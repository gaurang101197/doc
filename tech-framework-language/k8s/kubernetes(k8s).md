# Kubernetes (k8s)

## [Components](https://kubernetes.io/docs/concepts/overview/components/)
![components-of-kubernetes](https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg)

### `Nodes`
worker machines which run Pods.
#### `kubelet`
It makes sure that containers are running in a Pod. The kubelet takes a set of PodSpecs that are provided through various mechanisms and ensures that the containers described in those PodSpecs are running and healthy. The kubelet doesn't manage containers which were not created by Kubernetes.
#### `kube-proxy`
kube-proxy is a network proxy, implementing part of the Kubernetes Service concept. kube-proxy maintains network rules on nodes. These network rules allow network communication to your Pods from network sessions inside or outside of your cluster.
#### `Container runtime`
software that is responsible for running containers.

### `Control Plane`
The control plane's components make global decisions about the cluster (for example, scheduling), as well as detecting and responding to cluster events (for example, starting up a new pod when a deployment's replicas field is unsatisfied). Typically control plane components are run on the same machine, and user containers are not run on this machine. In production environments, the control plane usually runs across multiple computers, providing fault-tolerance and high availability.
#### `kube-apiserver`
The API server exposes an HTTP API that lets end users, different parts of your cluster, and external components communicate with one another. Most operations can be performed through the kubectl command-line interface or other command-line tools, such as kubeadm, which in turn use the API. However, you can also access the API directly using REST calls.
#### [`etcd`](https://etcd.io/)
A distributed, reliable key-value store for all cluster data.
#### `kube-scheduler`
selects a node for Pods to run on.
#### `kube-controller-manager`
runs controller processes.
- `Node controller`: Responsible for noticing and responding when nodes go down.
- `Job controller`: Watches for Job objects that represent one-off tasks, then creates Pods to run those tasks to completion.
- `EndpointSlice controller`: Populates EndpointSlice objects (to provide a link between Services and Pods).
  1. Iterate through existing EndpointSlices, remove endpoints that are no longer desired and update matching endpoints that have changed.
  2. Iterate through EndpointSlices that have been modified in the first step and fill them up with any new endpoints needed.
  3. If there's still new endpoints left to add, try to fit them into a previously unchanged slice and/or create new ones.
- `ServiceAccount controller`: Create default ServiceAccounts for new namespaces.
#### `cloud-controller-manager`
embeds cloud-specific control logic. The cloud-controller-manager only runs controllers that are specific to your cloud provider. If you are running Kubernetes on your own premises, or in a learning environment inside your own PC, the cluster does not have a cloud controller manager. As with the kube-controller-manager, the cloud-controller-manager combines several logically independent control loops into a single binary that you run as a single process. You can scale horizontally (run more than one copy) to improve performance or to help tolerate failures. The following controllers can have cloud provider dependencies:
- `Node controller`: For checking the cloud provider to determine if a node has been deleted in the cloud after it stops responding
- `Route controller`: For setting up routes in the underlying cloud infrastructure
- `Service controller`: For creating, updating and deleting cloud provider load balancers


## Concepts

### [EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/)

- You link an EndpointSlice to a Service by setting the `kubernetes.io/service-name` label on that EndpointSlice.
- The control plane automatically creates EndpointSlices for any Kubernetes Service that has a selector specified. These EndpointSlices include references to all the Pods that match the Service selector.
- EndpointSlices group network endpoints together by unique combinations of protocol(e.g. TCP), port number, and Service name.
- By default, the control plane creates and manages EndpointSlices to have no more than 100 endpoints each. You can configure this with the `--max-endpoints-per-slice` kube-controller-manager flag, up to a maximum of 1000.
- EndpointSlices can act as the source of truth for kube-proxy when it comes to how to route internal traffic. 

### [Endpoints](https://kubernetes.io/docs/concepts/services-networking/service/#endpoints)
In the Kubernetes API, an Endpoints (the resource kind is plural) defines a list of network endpoints, typically referenced by a Service to define which Pods the traffic can be sent to.

### [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- If some set of Pods (call them "backends") provides functionality to other Pods (call them "frontends") inside your cluster, how do the frontends find out and keep track of which IP address to connect to, so that the frontend can use the backend part of the workload?
- The controller for Service continuously scans for Pods that match its selector, and then makes any necessary updates to the set of EndpointSlices for the Service.

**Types of Service:**
#### `ClusterIP`
Exposes the Service on a cluster-internal IP. Choosing this value makes the Service only reachable from within the cluster. You can expose the Service to the public internet using an Ingress or a Gateway.
#### `NodePort`
#### `LoadBalancer`
#### `ExternalName`

## kubectl
### cheat sheet
```bash
# k=kubectl
-A options for
k cluster-info

# -A = all namespace
# -n namespace_name
k get pods 
# k get pods -o wide => get ip address of pod
k get services
k get nodes
k get ns/namespace
k get deployments
k get rs/replicaSet

k apply -f file_name.yaml
k delete -f file_name.yaml

k delete pod pod-name -n namespace

# useful to pod event logs
k describe pod pod-name -n namespace

k exec -it pod-name -- /bin/bash

k logs pod-name -f --tail=10 --timestamps
# -c, to specify container name if you have multiple container within pod
```

## References
1. 