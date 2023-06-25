# Kubernetes (k8s)

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
k get namespace/ns
k get deployments

k apply -f file_name.yaml
k delete -f file_name.yaml

k delete pod pod-name -n namespace

# useful to pod event logs
k describe pod pod-name -n namespace

k exec -it pod-name -- /bin/bash
```

## References
1. 