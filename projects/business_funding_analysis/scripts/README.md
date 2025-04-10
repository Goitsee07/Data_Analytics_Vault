
# Business Funding Analysis Script 💻  
`business_funding_analysis.py`  

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Dependencies](https://img.shields.io/badge/dependencies-Pandas%20%7C%20Matplotlib%20%7C%20Seaborn-orange)](https://github.com/Goitsee07/Analytics_Vault/blob/main/requirements.txt)

A Python script to clean, analyze, and visualize South African business funding data. Part of a data analytics portfolio.

---

## 🚀 Features  
- **Data Cleaning**: Handles messy financial formats (`$1.9b` → `1900000000`)  
- **Automated Analysis**: Calculates key metrics (total/average funding)  
- **Visualizations**: Generates charts for trends and sector comparisons  
- **Local Focus**: Optimized for SA business data  

---

## ⚙️ Requirements  
```bash
pip install pandas matplotlib seaborn
```

---

## 🛠️ Usage  
### 1. Clone the Repository  
```bash
git clone https://github.com/Goitsee07/Analytics_Vault.git
cd Analytics_Vault/projects/business_funding_analysis/scripts
```

### 2. Run the Script  
```bash
python business_funding_analysis.py
```

### 3. Expected Output  
```
✅ STEP 1: Loaded 26 records!
✅ STEP 2: Cleaned 23 valid records!
✅ STEP 3: Saved cleaned data to /data/cleaned/

📊 Total Funding: R4.35B
📊 Average Deal Size: R189.31M
🏆 Top Sector: private_equity
```

---

## 📂 Input/Output  
| | |  
|---|---|  
**Input** | `data/raw/Business Funding Data.csv`  
**Output** | `data/cleaned/cleaned_business_funding.csv`  
**Visuals** | `visuals/top_sectors.png`, `visuals/funding_timeline.png`  

---

## 🔑 Key Functions  
```python
def clean_amount(amount_str: str) -> float:
    """Converts $1.9b → 1900000000.0""" 

def generate_visuals(df: pd.DataFrame) -> None:
    """Produces 3 analysis charts"""
```

---

## 🐛 Troubleshooting  
**Error** | **Solution**  
---|---  
`FileNotFoundError` | Check file paths in `/data/raw/`  
`ModuleNotFoundError` | Run `pip install -r requirements.txt`  
`KeyError` | Verify column names in raw CSV match `Amount`, `Categories`  

---

## 🌍 Related Links  
- [Full Project README](../README.md)  
- [Jupyter Notebook Version](../notebooks/Business_Funding_Analysis.ipynb)  

---

📬 **Contact**: [goitsee07@gmail.com](mailto:goitsee07@gmail.com) | [LinkedIn](https://linkedin.com/in/goitseendlovu)  

---
