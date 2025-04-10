
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
