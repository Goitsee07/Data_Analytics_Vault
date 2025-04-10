
# Data Documentation 📊

## Raw Data (`raw/`)
- `Business Funding Data.csv` - Original dataset
- **Columns**: 11 including:
  - `Amount`: Raw funding strings ($1.9b)
  - `Investors`: Comma-separated list
  - `Categories`: List-formatted sectors

## Cleaned Data (`cleaned/`)
- `cleaned_business_funding.csv` - Processed version
- **Improvements**:
  - Standardized currency to ZAR
  - Exploded list columns
  - Added `amount_clean` numeric column

## 🔄 Update Process
```mermaid
graph LR
A[Raw Data] --> B(Cleaning Script)
B --> C[Cleaned CSV]
C --> D[Analysis]

### **4. Scripts README.md** (`projects/business_funding_analysis/scripts/README.md`)
```markdown
# Analysis Scripts 🐍

## File Structure
```
scripts/
├── business_funding_analysis.py  # Main script
└── helpers.py                    # Utility functions
```

## Main Functions
```python
def clean_amount(amount_str: str) -> float:
    """Converts $1.9b → 1900000000.0"""
    
def generate_visuals(df: pd.DataFrame) -> None:
    """Produces 6 analysis charts"""
```

## ▶️ Execution
```bash
# Install dependencies
pip install pandas matplotlib seaborn

# Run analysis (outputs to ../visuals/)
python business_funding_analysis.py
```

## 🧪 Testing
```python
# Sample test case
def test_clean_amount():
    assert clean_amount("$1.9b") == 1900000000.0
```
