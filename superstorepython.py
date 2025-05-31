import pandas as pd

# Load the dataset
df = pd.read_csv('superstoredata.csv')
print('Original Shape:', df.shape)

# Convert date columns to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# Drop rows with missing Order Date or Ship Date
df = df.dropna(subset=['Order Date', 'Ship Date'])

# Drop rows with missing Postal Code
df = df.dropna(subset=['Postal Code'])

# Drop unnecessary columns
df = df.drop(columns=['Row ID', 'Country', 'Customer Name'])

# Create time-based features
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month-Year'] = df['Order Date'].dt.to_period('M').astype(str)

# Save cleaned dataset
df.to_csv('Cleaned_Superstore.csv', index=False)
print("Cleaned dataset saved as 'Cleaned_Superstore.csv'")
