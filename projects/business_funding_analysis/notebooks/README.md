
# Business Funding Analysis Notebook 📊

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Goitsee07/Analytics_Vault/blob/main/projects/business_funding_analysis/notebooks/Business_Funding_Analysis.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Goitsee07/Analytics_Vault/HEAD?labpath=projects%2Fbusiness_funding_analysis%2Fnotebooks%2FBusiness_Funding_Analysis.ipynb)

Interactive analysis of South African business funding trends. Part of my Data Analytics portfolio.

![Top Sectors](https://github.com/Goitsee07/Analytics_Vault/raw/main/projects/business_funding_analysis/visuals/top_sectors.png)

## Features
- **Local Focus**: Analyzes R4.35B+ in SA business funding
- **Interactive**: Modify code and see real-time results
- **Visual Storytelling**: Dynamic charts and graphs
- **Open Source**: Free to use and modify

## How to Use
### 1. Quick Preview
Click the **Colab** or **Binder** badge above to run directly in your browser.

### 2. Local Setup
```bash
git clone https://github.com/Goitsee07/Analytics_Vault.git
cd Analytics_Vault/projects/business_funding_analysis/notebooks
jupyter notebook Business_Funding_Analysis.ipynb
```

## Notebook Structure
1. **Data Loading**: 
   - Direct import from GitHub
   - Initial data exploration

2. **Data Cleaning**:
   - Handle missing values
   - Fix date formats
   - Standardize categories

3. **Analysis**:
   ```python
   # Sample code snippet
   df.groupby('Categories')['amount_clean'].sum().nlargest(5)
   ```

4. **Visualization**:
   - Sector comparisons
   - Funding timelines
   - Investor relationships

![Funding Timeline](https://github.com/Goitsee07/Analytics_Vault/raw/main/projects/business_funding_analysis/visuals/funding_timeline.png)

## Requirements
```python
# Python 3.10+ required
pip install -r ../../requirements.txt
```
**Packages**: pandas, matplotlib, seaborn, jupyter

## Key Findings
- **Top Sector**: Private Equity (42% of total funding)
- **Peak Funding**: Q2 2024 (R1.2B in June)
- **Investor Pattern**: 3+ investors → 4.7× higher funding

## Contributing
1. Fork this repository
2. Create your branch: `git checkout -b new-feature`
3. Commit changes: `git commit -m 'Add awesome feature'`
4. Push: `git push origin new-feature`
5. Submit a pull request

**Report Issues**: [GitHub Issues](https://github.com/Goitsee07/Analytics_Vault/issues)

---

📬 Contact: [goitsee07@gmail.com](mailto:goitsee07@gmail.com) | [LinkedIn](https://linkedin.com/in/goitseendlovu)
