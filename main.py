import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

amazone1 = pd.read_csv("Amazon Sales data.csv")
print(amazone1.head())

# Load the data (replace with your dataset)
# For simplicity, we'll create a DataFrame with example data

data = {
    'date': ['2021-01-01', '2021-02-01', '2021-03-01'],
    'sales_amount': [1000, 1500, 1200]
}

amazone = pd.DataFrame(amazone1)

# Convert 'date' to datetime and extract month and year
amazone['date'] = pd.to_datetime(amazone['Order Date'])
amazone['month'] = amazone['date'].dt.month
amazone['year'] = amazone['date'].dt.year

Total_Cost = amazone['Total Cost']



# Calculate yearly_month-wise sales
amazone['year_month'] = amazone['date'].dt.to_period('M')

# Calculate total sales per month and year
monthly_sales = amazone.groupby('month')['Units Sold'].sum()
yearly_sales = amazone.groupby('year')['Unit Cost'].sum()
yearly_monthly_sales = amazone.groupby('year_month')['Unit Cost'].sum()

# Visualize sales trends
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
monthly_sales.plot(kind='bar', title='Monthly Sales')
plt.subplot(2, 2, 2)
yearly_sales.plot(kind='bar', title='Yearly Sales')
plt.subplot(2, 2, 3)
yearly_monthly_sales.plot(kind='bar', title='Yearly-Monthly Sales')
plt.tight_layout()
plt.show()
