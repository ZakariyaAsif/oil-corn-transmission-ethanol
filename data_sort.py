import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Download data
oil = yf.download("CL=F", start="2000-01-01")
corn = yf.download("ZC=F", start="2000-01-01")
gas = yf.download("RB=F", start="2000-01-01")

# Save raw data
oil.to_csv('../data_raw/oil.csv')
corn.to_csv('../data_raw/corn.csv')
gas.to_csv('../data_raw/gasoline.csv')

# Load raw CSVs
oil_raw = pd.read_csv("../data_raw/oil.csv", header=[0, 1], index_col=0)
corn_raw = pd.read_csv("../data_raw/corn.csv", header=[0, 1], index_col=0)
gas_raw = pd.read_csv("../data_raw/gasoline.csv", header=[0, 1], index_col=0)

# Keep only close prices
oil = oil_raw[['Close']].copy()
corn = corn_raw[['Close']].copy()
gas = gas_raw[['Close']].copy()

# Rename columns
oil.columns = ['Oil']
corn.columns = ['Corn']
gas.columns = ['Gasoline']

# Reset index
oil = oil.reset_index()
corn = corn.reset_index()
gas = gas.reset_index()

# Convert dates
oil['Date'] = pd.to_datetime(oil['Date'])
corn['Date'] = pd.to_datetime(corn['Date'])
gas['Date'] = pd.to_datetime(gas['Date'])

# Sort and remove duplicates
oil = oil.sort_values('Date').drop_duplicates(subset='Date')
corn = corn.sort_values('Date').drop_duplicates(subset='Date')
gas = gas.sort_values('Date').drop_duplicates(subset='Date')

# Merge datasets
df = oil.merge(corn, on='Date', how='inner')
df = df.merge(gas, on='Date', how='inner')

# Convert to numeric
df['Oil'] = pd.to_numeric(df['Oil'], errors='coerce')
df['Corn'] = pd.to_numeric(df['Corn'], errors='coerce')
df['Gasoline'] = pd.to_numeric(df['Gasoline'], errors='coerce')

# Drop missing values
df = df.dropna(subset=['Oil', 'Corn', 'Gasoline'])

# Remove nonpositive values
df = df[(df['Oil'] > 0) & (df['Corn'] > 0) & (df['Gasoline'] > 0)]

# Compute log returns
df['Oil_ret'] = np.log(df['Oil'] / df['Oil'].shift(1))
df['Corn_ret'] = np.log(df['Corn'] / df['Corn'].shift(1))
df['Gasoline_ret'] = np.log(df['Gasoline'] / df['Gasoline'].shift(1))

# Drop NaNs created by shift
df = df.dropna()

# Remove extreme outliers
df = df[(df['Corn_ret'] > -0.2) & (df['Corn_ret'] < 0.2)]
df = df[(df['Oil_ret'] > -0.6) & (df['Oil_ret'] < 0.6)]
df = df[(df['Gasoline_ret'] > -0.4) & (df['Gasoline_ret'] < 0.4)]

# Correlation matrix
print(df[['Oil_ret', 'Corn_ret', 'Gasoline_ret']].corr())

# Histograms
df[['Oil_ret', 'Corn_ret', 'Gasoline_ret']].hist(
    bins=100,
    figsize=(12, 4)
)

# Rolling correlation
rolling_corr = df['Oil_ret'].rolling(30).corr(df['Gasoline_ret'])

rolling_corr.plot(figsize=(10, 4))
plt.title("30-Day Rolling Correlation: Oil vs Gasoline")
plt.show()

# Save cleaned dataset
df.to_csv('../data_clean/merged_returns.csv', index=False)
