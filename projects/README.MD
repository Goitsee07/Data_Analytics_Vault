# Business Funding Analysis - South Africa 🇿🇦

![Project Banner](visuals/top_sectors.png)

## 📌 Overview
Analysis of R2.5B+ in business funding across South African companies. Identifies key investment trends, top sectors, and investor patterns.

## 🔑 Key Insights
- Private Equity dominates funding (42% of total)
- Average deal size: R189 million
- 78% of large deals (>R500M) involve multiple investors

## 📂 Dataset
| | |
|---|---|
**Source** | [Kaggle Business Funding Data](https://www.kaggle.com/datasets/techsalerator/business-funding-data-in-south-africa) |
**Raw Records** | 26 companies |
**Cleaned Data** | 23 valid entries |

## 📊 Key Visualizations
![Funding Timeline](visuals/funding_timeline.png)
*Funding distribution over 2024 showing Q2 peak*

![Investor Analysis](visuals/investor_count_vs_funding.png)  
*Correlation between investor count and funding size*

[View Full Report](Business_Funding_Analysis_Report.pdf)

## 🛠️ Technical Stack
```python
# Sample cleaning code
def clean_amount(amount_str):
    # Handles $1.9b → 1900000000
    pass
