# [VictoriaMetrics](https://victoriametrics.com/)

## [setting up victoriadb locally](https://docs.victoriametrics.com/Quick-Start.html#starting-vm-cluster-via-docker)
``` bash
docker pull victoriametrics/victoria-metrics:latest
docker run -it --rm -v `pwd`/victoria-metrics-data:/victoria-metrics-data -p 8081:8428 victoriametrics/victoria-metrics:latest
```

## Publishing metrics locally

1. push metrics using HTTP

``` bash
curl -d 'latency,tag1=value1,tag2=value2 field1=123,field2=1.23' -X POST 'http://localhost:8081/write'

curl -d '{"metric":{"__name__":"latency","tag1":"value1","tag2":"value2"},"values":[1.23],"timestamps":[1676626627000]}' -X POST http://localhost:8081/api/v1/import
```

``` python
import requests
push = requests.post('http://localhost:8081/api/v1/import',
                     data={"metric": {"__name__": "latency", "tag1": "value1", "tag2": "value2"}, "values": [1.23], "timestamps": [1676626627000]})
push.status_code == requests.codes.no_content

values=[1657.1860370635986]
timestamps=[1677474000000.0]
tag1="value1"
tag2="value"
env="staging"
metric={"__name__": "latency", "env": env, "tag1": tag1, "tag2": tag2}
requests.post("http://localhost:8081" + '/api/v1/import', data=json.dumps({"metric": metric, "values": values, "timestamps": timestamps}), verify=False)
```

2. Verify published metrics
```bash
curl -G 'http://vm_host:8081/api/v1/export' -d 'match={__name__=~"latency.*"}'
```
``` python
import requests
export = requests.get('http://vm_host:8081/api/v1/export',
                      params={'match': '{__name__=~"latency.*"}'})
```