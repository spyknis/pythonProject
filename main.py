import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("finance_liquor_sales.csv")


# Remove rows with any missing value
data = data.dropna()
# Remove columns with any missing value
data = data.dropna(axis=1)

# Convert the date
data['date'] = pd.to_datetime(data['date'])
# Filter the data
mask = (data['date'] >= '2016-01-01') & (data['date'] <= '2019-12-31')
selected_data = data[mask]
print(selected_data)

# Group by zip code and find the most popular item
most_popular_item = data.groupby('zip_code')['item_number'].agg(lambda x: x.value_counts().idxmax())

# Group by store and calculate the percentage of sales
total_sales_per_store = data.groupby('store_name')['sale_dollars'].sum()
percentage_of_sales = total_sales_per_store / total_sales_per_store.sum() * 100

# Print the results
print("Most popular item per zipcode:")
print(most_popular_item)
print("Percentage of sales per store:")
print(percentage_of_sales)

# Visualize the most popular item per zip code
plt.figure(figsize=(10, 6))
most_popular_item.plot(kind='bar')
plt.xlabel('Zip Code')
plt.ylabel('Most Popular Item')
plt.title('Most Popular Item per Zip Code')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualize the percentage of sales per store
plt.figure(figsize=(10, 6))
percentage_of_sales.plot(kind='bar')
plt.xlabel('Store')
plt.ylabel('Percentage of Sales')
plt.title('Percentage of Sales per Store')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()





