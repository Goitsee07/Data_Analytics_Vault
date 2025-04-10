# business_funding_analysis.py (Mobile-Optimized)
import pandas as pd
import re
import sys
from ast import literal_eval

def log(message):
    """Mobile-friendly logging"""
    print(f"[*] {message}")

try:
    # =====================
    # 1. Load Data
    # =====================
    log("Loading data...")
    df = pd.read_csv("/storage/emulated/0/Download/Business Funding Data.csv", 
                    encoding='latin1')
    log(f"Loaded {len(df)} records")

    # =====================
    # 2. Clean Data
    # =====================
    def clean_amount(amount_str):
        """Simplified mobile-friendly cleaner"""
        try:
            amount_str = str(amount_str).lower()
            match = re.search(r"[\d\.]+", amount_str)
            value = float(match.group(0)) if match else None
            
            if 'b' in amount_str:
                return value * 1e9
            elif 'm' in amount_str:
                return value * 1e6
            return value
            
        except:
            return None

    log("Cleaning amounts...")
    df['amount_clean'] = df['Amount'].apply(clean_amount)
    df = df.dropna(subset=['amount_clean'])
    log(f"{len(df)} valid records after cleaning")

    # =====================
    # 3. Basic Analysis
    # =====================
    log("\n=== Results ===")
    print(f"Average funding: R{df['amount_clean'].mean():,.2f}")
    print(f"Top sector: {df['Categories'].value_counts().idxmax()}")
    
    # Save cleaned data
    df.to_csv("/storage/emulated/0/Download/cleaned_funding.csv", index=False)
    log("Saved cleaned data to Download folder")

except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)