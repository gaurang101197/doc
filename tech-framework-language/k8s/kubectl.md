# kubectl

## cheat sheet

```bash
# k=kubectl

k api-resources
k cluster-info

# -A = all namespace
# -n namespace_name
k get pods 
# get ip address of pod
k get pods -o wide
# get all object of particular namespace
k get all -n metric
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

# -c, to specify container name if you have multiple container within pod
k logs pod-name -f --tail=10 --timestamps

# Cleans up any failed pods in your-namespace
kubectl delete pods --field-selector status.phase=Failed -n <your-namespace>

# Forward one or more local ports (sourcePort:targetPort) to a pod.
# k port-forward type/name 8081:8080
k port-forward service/kube-state-metrics 8081:8080 -n metric
```
