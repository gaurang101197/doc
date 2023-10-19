# Elastic Search

Elasticsearch is a distributed search and analytics engine built on [Apache Lucene](https://lucene.apache.org/).  
Elasticsearch is a document store.

## ELK stack

1. **Integrations**  
Variety of methods to ingest data.

2. **Elastic search**  
Elasticsearch is a distributed and RESTful search engine.

3. **Kibana**  
Kibana is a data visualization and exploration tool.

## Architecture

![architecture diagram](./elastic-search-architecture-diagram.webp)

- **Node**: A single instance of elasticsearch.
- **Cluster**: A collection of nodes, working together.
- **Index**: A container for documents within the cluster, consist of shards.
- **Shard**: The unit at which Elasticsearch distributes data around the cluster.
- **Document**: Data structure to store data (JSON).
