# OLAP vs OLTP

| Criteria | OLAP (Online Analytical Processing) | OLTP (Online Transaction Processing) |
| --- | --- | --- |
| | Combines and groups the data to **analyze** it. | **Updates** transactional data reliably and efficiently. |
| Data Architecture | OLAP database architecture prioritizes **data read over data write** operations. You can quickly and efficiently perform complex queries on large volumes of data. | OLTP database architecture **prioritizes data write operations**. It’s optimized for write-heavy workloads and can update high-frequency, high-volume transactional data without compromising data integrity. |
| Data Processing | **Batch** OLAP processing times can vary from minutes to hours depending on the type and volume of data being analyzed. To update an OLAP database, you periodically process data in large batches then upload the batch to the system all at once. Data update frequency also varies between systems, from daily to weekly or even monthly. | **Realtime** OLTP databases manage database updates in real time (in milliseconds or less). |
| Volume of data | OLAP has large storage requirements. Think terabytes (TB) and petabytes (PB). | OLTP has comparatively smaller storage requirements. Think gigabytes (GB). |
| Response time | OLAP has longer response times, typically in seconds or minutes. | OLTP has shorter response times, typically in milliseconds. |
| Example applications | OLAP is good for analyzing trends, predicting customer behavior, and identifying profitability. | OLTP is good for processing payments, customer data management, and order processing. |
| Example database | Apache Druid, Snowflake, Apache Hive, PrestoDB, ClickHouse | MySQL, PostgreSQL |

## Example

Let's consider a large retail company that operates hundreds of stores across the country. The company has a massive database that tracks sales, inventory, customer data, and other key metrics.

| OLAP | OLTP |
| --- | --- |
| The company uses OLTP to process transactions in real time, update inventory levels, and manage customer accounts. Each store is connected to the central database, which updates the inventory levels in real time as products are sold. The company also uses OLTP to manage customer accounts—for example, to track loyalty points, manage payment information, and process returns. | The company uses OLAP to analyze the data collected by OLTP. The company’s business analysts can use OLAP to generate reports on sales trends, inventory levels, customer demographics, and other key metrics. They perform complex queries on large volumes of historical data to identify patterns and trends that can inform business decisions. They identify popular products in a given time period and use the information to optimize inventory budgets. |