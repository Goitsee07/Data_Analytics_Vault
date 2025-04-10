# Business Funding Analysis - South Africa 🇿🇦

![Project Banner](visuals/top_sectors.png)

## 📌 Project Overview
Analysis of R2.5B+ in business funding across South African companies, identifying investment trends and sector patterns. Features automated data cleaning and professional visualizations.

## 🔑 Key Insights
- **Top Sector**: Private Equity (42% of total funding)
- **Average Deal Size**: R189 million
- **Largest Deal**: R1.9B (Trafigura)
- **Investor Impact**: 3+ investors → 4.7× higher funding

## 🛠️ Technical Implementation
**Tools Used**:
- Python 3.11 | Pandas | Regex
- Matplotlib | Seaborn
- GitHub Actions (Automation)

![Analysis Workflow](visuals/funding_distribution.png)

## 📊 Featured Visualizations
1. **Funding Timeline**  
   ![Funding Timeline](visuals/funding_timeline.png)
   - Shows 2024 quarterly trends
   - Q2 peak: R1.2B in June

2. **Investor Analysis**  
   ![Investor Chart](visuals/investor_count_vs_funding.png)
   - Strong correlation (r=0.78)
   - Multi-investor deals dominate

3. **Sector Breakdown**  
   ![Sectors](visuals/total_funding_by_category.png)
   - Venture capital = 38%
   - Seed funding = 22%

## ▶️ How to Use
1. Install requirements:
   ```bash
   pip install pandas matplotlib seaborn
   ```
2. Run analysis:
   ```bash
   python scripts/business_funding_analysis.py
   ```
3. Outputs:
   - Cleaned data: `/data/cleaned`
   - Visuals: `/visuals`
   - Report: `Business_Funding_Analysis_Report.pdf`

## 📂 Folder Contents
- `/data` - Raw CSV + Cleaned datasets
- `/scripts` - Python cleaning/analysis code
- `/visuals` - Generated charts (PNG)
- `/notebooks` - Interactive Jupyter analysis

## 📫 Contact
**Author**: Goitseone Ndlovu  
**Email**: goitsee07@gmail.com  
[LinkedIn Profile](https://www.linkedin.com/in/goitseendlovu) | [GitHub Profile](https://github.com/Goitsee07)

---

