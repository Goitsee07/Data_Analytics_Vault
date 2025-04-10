# Business Funding Analysis (South Africa)  
**Goal**: Analyze funding trends and key sectors using messy, real-world data.  

## 🔍 Key Insights  
1. **Top Sectors**: Private equity and venture capital dominate funding.  
2. **Funding Distribution**: Most deals are under R50 million, with a few large outliers.  
3. **Trends**: Funding peaked in [Year] due to [hypothesis based on data].  

## 📊 Visualizations  
![Top Sectors](visuals/top_sectors.png)  
*Figure 1: Top 10 sectors by total funding*  

![Funding Trends](visuals/funding_trends.png)  
*Figure 2: Yearly funding trends*  

## 🛠️ Tools & Techniques  
- **Data Cleaning**: Regex for messy amounts (`$1.9b` → `1,900,000,000`)  
- **Visualization**: Matplotlib/Seaborn  
- **Analysis**: Time-series trends, sector comparisons  

## ▶️ How to Run  
```bash
git clone https://github.com/Goitsee07/data_analyst_portfolio
cd projects/business_funding_analysis/scripts
python business_funding_analysis.py
