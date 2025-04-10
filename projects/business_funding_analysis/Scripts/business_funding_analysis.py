import pandas as pd
import re
from ast import literal_eval
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------------------------------
# 1. Load Data
# ----------------------------------------------------------------------------------
def load_data():
    url = "https://github.com/Goitsee07/Analytics_Vault/raw/main/projects/business_funding_data/Business%20Funding%20Data.csv"
    data = pd.read_csv(url, encoding='latin1')
    print("✅ Data loaded successfully!")
    return data

# ----------------------------------------------------------------------------------
# 2. Clean Data
# ----------------------------------------------------------------------------------
def clean_amount(amount_str):
    try:
        # Remove unwanted characters
        cleaned = re.sub(r"[^0-9\.\$€£mbMB]", "", str(amount_str))
        
        # Extract first valid amount
        match = re.search(r"[\$€£]?([\d\.]+)([mbMB]?)", cleaned)
        if not match:
            return None
            
        value = float(match.group(1))
        suffix = match.group(2).lower()
        
        # Apply multipliers
        if suffix == "m":
            value *= 1_000_000
        elif suffix == "b":
            value *= 1_000_000_000
            
        return value
    except:
        return None

def clean_categories(cat_str):
    try:
        return literal_eval(str(cat_str))
    except:
        return [str(cat_str)]

def process_data(data):
    # Clean amounts
    data["amount_clean"] = data["Amount"].apply(clean_amount)
    data = data.dropna(subset=["amount_clean"])
    
    # Clean categories
    data["Categories"] = data["Categories"].apply(clean_categories)
    data = data.explode("Categories")
    
    print("✅ Data cleaned successfully!")
    return data

# ----------------------------------------------------------------------------------
# 3. Visualizations
# ----------------------------------------------------------------------------------
def create_visuals(data):
    sns.set_theme(style="whitegrid", palette="pastel")
    
    # Visualization 1: Top Sectors
    plt.figure(figsize=(10,6))
    top_sectors = data.groupby("Categories")["amount_clean"].sum().sort_values(ascending=False).head(10)
    top_sectors.plot(kind='bar')
    plt.title("Top 10 Sectors by Funding (ZAR)", fontsize=14)
    plt.xlabel("Sector", fontsize=12)
    plt.ylabel("Total Funding (Billions)", fontsize=12)
    plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"R{x/1e9:.1f}B"))
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("top_sectors.png")
    plt.close()
    
    # Visualization 2: Funding Distribution
    plt.figure(figsize=(10,6))
    sns.boxplot(x=data["amount_clean"].apply(lambda x: x/1e6))
    plt.title("Funding Distribution (Millions ZAR)", fontsize=14)
    plt.xlabel("Funding Amount (Millions)", fontsize=12)
    plt.tight_layout()
    plt.savefig("funding_distribution.png")
    plt.close()
    
    # Visualization 3: Time Trends (if available)
    if 'Effective date' in data.columns:
        plt.figure(figsize=(10,6))
        data['year'] = pd.to_datetime(data['Effective date']).dt.year
        yearly_funding = data.groupby('year')['amount_clean'].sum()
        yearly_funding.plot(kind='line', marker='o', color='purple')
        plt.title("Funding Trends Over Time", fontsize=14)
        plt.xlabel("Year", fontsize=12)
        plt.ylabel("Total Funding (Billions ZAR)", fontsize=12)
        plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, _: f"R{x/1e9:.1f}B"))
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("funding_trends.png")
        plt.close()
    
    print("✅ Visualizations saved as PNG files!")

# ----------------------------------------------------------------------------------
# Main Execution
# ----------------------------------------------------------------------------------
if __name__ == "__main__":
    # Load and process data
    df = load_data()
    cleaned_df = process_data(df)
    
    # Generate visuals
    create_visuals(cleaned_df)
    
    # Save cleaned data
    cleaned_df.to_csv("cleaned_business_funding.csv", index=False)
    print("✅ Cleaned data saved to 'cleaned_business_funding.csv'")
    print("\n=== Analysis Complete ===")
