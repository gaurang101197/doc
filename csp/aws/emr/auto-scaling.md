# EMR auto scaling

The following metrics indicate the current or target capacities of a cluster:
- TotalUnitsRunning
- CoreUnitsRequested
- CoreUnitsRunning
- TaskUnitsRequested
- TaskUnitsRunning

The following metrics indicate the usage status of cluster and applications:
- AppsCompleted (count)
- AppsPending (count)
- AppsRunning (count)
- ContainerAllocated (count)
- ContainerPending (count)
- IsIdle
    - It is set to 1 if no tasks are running and no jobs are running, and set to 0 otherwise. This value is checked at five-minute intervals and a value of 1 indicates only that the cluster was idle when checked, not that it was idle for the entire five minutes.
- MemoryAvailableMB
- MRActiveNodes

## useful for scaling cluster resources
- ContainerPendingRatio (ContainerPending/ContainerAllocated) (count)
    - If ContainerAllocated = 0, then ContainerPendingRatio = ContainerPending.
    - The value of ContainerPendingRatio represents a number, not a percentage.
- YARNMemoryAvailablePercentage
    - The percentage of remaining memory available to YARN (YARNMemoryAvailablePercentage = MemoryAvailableMB / MemoryTotalMB).
- HDFSUtilization (Percent)
    - The percentage of HDFS storage currently used.

Scaling up
- YARNMemoryAvailablePercentage <= 20 
- ContainerPendingRatio >= 1 
- HDFSUtilization >= 80 
- CapacityRemainingGB <= 20

Scaling Down
- YARNMemoryAvailablePercentage >= 80
- ContainerPendingRatio <= 0
- HDFSUtilization <= 20
- IsIdle >= 1

## Scaling related Q&A

> Q. What is the frequency of checking cluster metrics ?

A. https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-scale-on-demand.html

> Q. Suppose frequency is 1 minutes for one rule, rule get successfully executed and managed scaling determine it need to scale up the cluster, and it added X nodes to cluster, now after 1 minute again rule is fired to check whether scale up is required or not, but the X nodes which are added might not come up in 1 minutes, and metrics might be the same of cluster, so in this case rule will succeeded again, so does managed scaling handle such scenarios ?

A. Yes. These scenarios are handled internally and documentation is not available.

> Q. How does managed scaling determine the number of nodes to add or remove ?

A. EMR managed scaling will keep on adding instances until corresponding cloudwatch metrics reaches above threshold values and later again will check required cloudwatch metrics to trigger scaling is required or not . how many nodes at a time system chooses , that information documentation is not available.


## Optimisation on spark executor
- https://spark.apache.org/docs/latest/configuration.html#dynamic-allocation
- https://spark.apache.org/docs/latest/job-scheduling.html#dynamic-resource-allocation

## Things to check when you have problem in auto scaling emr with spark job

If your YARN jobs are intermittently slow during scale down and YARN Resource Manager logs show that most of your nodes were deny listed during that time, you can adjust the decommissioning timeout threshold. Reduce the spark.blacklist.decommissioning.timeout from one hour to one minute to make the node available for other pending containers to continue task processing.

You should also set yarn.resourcemanager.nodemanager-graceful-decommission-timeout-secs to a larger value to ensure Amazon EMR doesn’t force terminate the node while the longest “Spark Task” is still running on the node. The current Default is 60 minutes, which means Yarn force terminates the container after 60 minutes once the node enters the decomissioning state.

Over-utilization of EBS volumes can cause Managed Scaling issues. We recommend that you maintain EBS volume below 90% utilization.

Reference:
- https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hadoop-task-config.html
- https://aws.amazon.com/blogs/big-data/best-practices-for-resizing-and-automatic-scaling-in-amazon-emr/


## Experimentation with dynamic resource allocation in Spark (spark.shuffle.service.fetch.rdd.enabled)
- spark.dynamicAllocation.enabled=true
- spark.dynamicAllocation.shuffleTracking.enabled=true
- spark.dynamicAllocation.initialExecutors=48
- spark.dynamicAllocation.maxExecutors=infinity
- spark.dynamicAllocation.minExecutors=0
- spark.dynamicAllocation.executorAllocationRatio=1
- spark.shuffle.service.enabled=false
    
Request policy (https://spark.apache.org/docs/latest/job-scheduling.html#request-policy)
- spark.dynamicAllocation.schedulerBacklogTimeout=60s
- spark.dynamicAllocation.sustainedSchedulerBacklogTimeout=30s
- spark.dynamicAllocation.cachedExecutorIdleTimeout=infinity
- spark.shuffle.service.fetch.rdd.enabled
- spark.dynamicAllocation.shuffleTracking.timeout=infinity
    
Executor removal policy (https://spark.apache.org/docs/latest/job-scheduling.html#remove-policy)
- spark.dynamicAllocation.executorIdleTimeout=60s


## Blacklisted node

When you see nodes are marked decommissioning on the yarn and spark marking these nodes as blacklist
Configs to look for
- `yarn.resourcemanager.nodemanager-graceful-decommission-timeout-secs`:
    - Default value: 3600
    - This is the maximum time in seconds to wait for running containers and applications to complete before transition a DECOMMISSIONING node into DECOMMISSIONED
    - yarn-site
- `spark.blacklist.decommissioning.enabled`:
    - Default value: true
    - When set to true, Spark deny lists nodes that are in the decommissioning state in YARN. Spark does not schedule new tasks on executors running on that node. Tasks already running are allowed to complete.
    - spark-defaults
- `spark.blacklist.decommissioning.timeout`: 
    - Default value: 1h
    - This is the maximum time that spark does not schedule new tasks on executors running on that node. Tasks already running are allowed to complete.
    - spark-defaults

By default, both the above timeouts are set as 1hr.

When managed scaling triggers a scale down, YARN will put nodes it wants to decommission in a "DECOMMISSIONING" state. Spark will detect this and add these nodes to a "blacklist". In this state, Spark will not assign any new tasks to the node and once all tasks are completed, YARN will finish decommissioning the node. If the task runs longer than `yarn.resourcemanager.nodemanager-graceful-decommission-timeout-secs`, the node is force terminated and task will be re-assigned to another node.

### Solutions

1. The recommended option is to lower `spark.blacklist.decommissioning.timeout` to make the node available for other pending containers to continue task processing. This can improve job run times. However, please note that if a task is assigned to this node, and YARN transitions from DECOMMISSIONING into DECOMMISSIONED, the task will fail and will need to be reassigned to another node. (In your case, by default this value is set to 1 hour as discussed above, and despite the node coming back to running state no task were scheduled in these nodes, so lowering this value should ensure that task are scheduled much faster in the nodes and it does not have to wait for 1 hr as to what is happening right now)
With `yarn.resourcemanager.nodemanager-graceful-decommission-timeout-secs`, consider increasing this from the default of 1 hr to the length of your longest running task. This is to ensure that YARN does not force terminate the node while the task is running and having it to re-run on another node.

2. You can also decrease the `yarn.resourcemanager.nodemanager-graceful-decommission-timeout-secs` to a lower value to Decommission the nodes faster. But the disadvantage is that this can impact the long-running tasks as the node will be decommissioned faster and will not wait long for the running tasks to finish. You also need to set the `spark.blacklist.decommissioning.timeout` equal or greater than the `yarn.resourcemanager.nodemanager-graceful-decommission-timeout-secs`.

References
- https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-configure.html
- https://aws.amazon.com/blogs/big-data/spark-enhancements-for-elasticity-and-resiliency-on-amazon-emr/
- https://aws.github.io/aws-emr-best-practices/features/managed_scaling/best_practices/
- https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-scaledown-behavior.html
