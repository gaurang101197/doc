# [Apache Hudi](https://hudi.apache.org/)

## Architecture

## Concepts

### Table Types

| Topic | [Copy On Write Table](https://hudi.apache.org/docs/concepts/#copy-on-write-table) | [Merge On Read Table](https://hudi.apache.org/docs/concepts/#merge-on-read-table) |
| :----: | :---- | :---- |
| Description | - File slices in Copy-On-Write table only contain the base/columnar file and each commit produces new versions of base files. In other words, we implicitly compact on every commit, such that only columnar data exists. </br> - Does not support **snapshot queries (near real-time data)**. | - Is a superset of copy on write. </br> - It still supports read optimized queries of the table by exposing only the base/columnar files in latest file slices. Additionally, it stores incoming upserts for each file group, onto a row based delta log, to support **snapshot queries (near real-time data)** by applying the delta log, onto the latest version of each file id on-the-fly during query time. </br> - A periodic **compaction** process reconciles these changes from the delta log and produces a new version of base file. </br> - It provides **reduced write amplification** at cost of running periodic compaction process. |
| When to use |  |  |


### Incremental Processing

Incremental Processing merely refers to writing mini-batch programs in streaming processing style.  

Typical batch jobs consume all input and recompute all output, every few hours. Typical stream processing jobs consume some new input and recompute new/changes to output, continuously/every few seconds. While recomputing all output in batch fashion can be simpler, it's wasteful and resource expensive. Hudi brings ability to author the same batch pipelines in streaming fashion, run every few minutes.

## FAQs

### When to use

If you are looking to quickly ingest data onto HDFS or cloud storage, Hudi can provide you tools to help. Also, if you have ETL/hive/spark jobs which are slow/taking up a lot of resources, Hudi can potentially help by providing an incremental approach to reading and writing data.

As an organization, Hudi can help you build an efficient data lake, solving some of the most complex, low-level storage management problems, while putting data into hands of your data analysts, engineers and scientists much quicker.

## References

1. [use cases](https://hudi.apache.org/docs/use_cases/)
2. [FAQs](https://hudi.apache.org/docs/faq)
3. 