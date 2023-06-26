# docker

## Setup docker on ubuntu
```bash
sudo apt install docker-compose
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo docker run hello-world
```
### Known Issues
> ERROR: docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
```bash
sudo service --status-all
sudo service docker --full-restart
sudo service docker status
```

> ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?
```bash
sudo groupadd -g 135 docker
sudo usermod -aG docker $USER
newgrp docker
```


> ERROR: Failed to Setup IP tables: Unable to enable NAT rule:  (iptables failed: iptables --wait -t nat -I POSTROUTING -s {{ip_address}}/16 ! -o br-44f093ca6705 -j MASQUERADE: iptables: No chain/target/match by that name.
```bash
sudo iptables -t filter -N DOCKER
sudo service docker restart
```

> docker: Error response from daemon: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: waiting for init preliminary setup: EOF: unknown. ERRO[0027] error waiting for container: context canceled 


> ERROR: failed to add IPv4 address ip_address/16 to bridge: file exists

https://github.com/microsoft/WSL/issues/6404#issuecomment-810538101

### Reference
1. https://docs.docker.com/engine/install/ubuntu/


## docker-compose

- `entrypoint`: shell script which is run on container start up
- `command`: is passed as argument to `entrypoint`

## docker cheatsheet

```bash
# to create tag
docker image tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

# To remove unused docker resources
docker system prune --volumes -a
```