# SLO-SLI-SLA

## Definitions

### Service Level Agreements (SLAs)
- is a contract that the service provider promises customers on service availability, performance, etc, as well as potential compensation if they fail to deliver.

### Service Level Objective (SLOs)
- is an internal goal that the service provider wants to reach. Usually, it’s similar to SLA but tighter. For example, if data availability threshold is set to 99.9% in SLA, then it should be 99.99% in SLO. If a service breaks SLO, on-call engineers need to react quickly to avoid it breaking SLA, otherwise, the company (or the team) will lose money (or reputation).
- Often, SLO contains more metrics than SLA. For instance, to achieve overall availability 99.9%, the team needs to monitor the up-time of a few internal tools and each of them has its own SLO threshold.

### Service Level Indicator (SLIs)
- A SLI is a quantity we measure to determine whether we comply with an SLO. Very commonly, SLIs measure either the success rate or performance of some operation, but an SLI can be just any metric.
- For an SLI to be interesting, it needs to be associated with a condition. For example, we can state that 99% of all operations must complete successfully or that 95% of all transactions must finish within one second.
- The choice of SLIs is based on the agreement made in SLA.


### Key things to keep in mind while designing SLO
#### SLO Windows
The time frame to measure. We say we allow ourselves to be out of compliance 1% of the time, but over what time frame? Selecting this time frame turns out to be a hard problem to solve. If we measure over a very short time, say 10 minutes, then insignificant glitches will constantly trigger alerts. Alternatively, if we measure over a longer time period, say 30 days, then we will be alerted too late and risk missing severe outages altogether.

#### Burn Rates
Let’s say our contract with our users states 99.9% availability over 30 days. That works out to an error budget of 43 minutes. If we burn down these 43 minutes in small increments of minor glitches, our users are probably still happy and productive. But what if we have a single outage of 43 minutes at a business-critical time? It’s safe to say our users would be pretty unhappy with that experience!

To solve this, we can introduce burn rates. The definition is simple: If we burn down precisely 43 minutes (0.1% of 30 days in minutes) in our example over 30 days, we call this a burn rate of one. If we burn it down twice as fast, e.g., in 15 days, the burn rate is two and so on. As you will see, this allows us to track the long-term compliance, and to alert on severe, short-term issues.

#### Multiple Windows?
One idea is to use multiple time windows for immediate alerts and longer-term trend observations. The problem is that if we select a one hour window, a 99% objective allows only 36 seconds of non-compliance. For a 99.9% objective, that number drops to 3.6 seconds! This would cause a lot of noisy alerts for minor glitches.

#### Multiple Windows, Multiple Burn Rates
One way to overcome this problem is to employ the burn rates we previously discussed above. If we are looking at a shorter time window, we measure against a faster burn rate. This allows us to fire alerts when a service has been unavailable for a meaningful amount of time. When we monitor over a longer time window, we use a slower burn rate to catch worrisome trends. The following table illustrates how this can be done.

This means that if we’re burning our error budget at a rate of 14.4 during an hour window, we should have fired off a critical alert. We select 14.4 because it represents a burn of 2% over an hour.

On the other hand, if we see a slow burn over a longer time, it may not have a severe impact on users, but it means that we’re on track to breach our SLO over a longer time. The first alert should cause someone to be paged immediately, while the second one can be a lower priority alert that someone can look at when they have time.

#### Key note
> long-term monitoring of an SLO trend and short-term alerting must be done using different methods.

### SLO for data pipelines
From the user stories, you probably get a feel of what data reliability means. We can break it down to several measurable metrics:
* Availability — whether the data is available. Things like network issues or infra issues can prevent users from accessing data.
* Freshness — how up-to-date your data tables are, as well as the rhythm when your tables are updated.
* (In)Completeness — the percentage of unexpected missing data entries, can be both on the row level and column level. For example, is there any row from the upstream tables not being processed? Is there any field in the destination table missing data for > X% of rows?
* Duplicates — the percentage of unexpected duplicated primary key(s).
* Distribution — the accepted range of certain fields. It can be an enumeration or a range of numbers.

#### How and where to start
1. Identify the services that are worth applying SLA to.
    - It could be a key dashboard showing company OKRs (Objectives and key results) or the most frequently used table within the organization.
2. Define what reliable data means together with your stakeholders.
    - To begin with, data engineers can assess the historical performance of the data to gain a baseline and understand its usage pattern
    - Engineers can ask stakeholders to think about their requirements for reliability. What do they care about the most? Freshness? Accuracy? Availability? Duplicates?
3. Define SLI to measure reliability.
4. Define SLO and set up alerts.

#### How to implement SLO ####
TODO:

## Reference
1. https://www.pagerduty.com/blog/wavefront-smart-slo/
2. https://towardsdatascience.com/its-time-to-set-sla-slo-sli-for-your-data-team-only-3-steps-ed3c93009aa5
