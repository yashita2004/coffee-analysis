
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("coffee1.csv")   # change path if needed


df['datetime_full'] = pd.to_datetime(df['date'] + " " + df['datetime'], errors='coerce')


df['date_only'] = df['datetime_full'].dt.date
df['hour'] = df['datetime_full'].dt.hour

daily_sales = df.groupby('date_only')['money'].sum()

plt.figure(figsize=(10,5))
daily_sales.plot(kind='line', marker='o', color="green")
plt.title("Daily Total Coffee Sales")
plt.xlabel("Date")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

hourly_sales = df.groupby('hour')['money'].sum()

plt.figure(figsize=(8,5))
hourly_sales.plot(kind='bar', color="skyblue")
plt.title("Total Sales by Hour of the Day")
plt.xlabel("Hour of Day")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.show()


avg_money_per_coffee = df.groupby('coffee_name')['money'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,5))
avg_money_per_coffee.plot(kind='bar', color="orange")
plt.title("Average Price per Coffee Type")
plt.ylabel("Average Money (₹)")
plt.xticks(rotation=45, ha="right")
plt.show()


plt.figure(figsize=(8,5))
plt.scatter(df.index, df['money'], alpha=0.5, color="purple")
plt.title("Scatter Plot of Coffee Prices")
plt.xlabel("Transaction Index")
plt.ylabel("Money Spent")
plt.show()
