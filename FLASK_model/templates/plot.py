import matplotlib.pyplot as plt
import seaborn as sns

# Plot sales over time
plt.figure(figsize=(12, 5))
plt.plot(dataFrame['date'], dataFrame['sales_volume'], label='Sales Volume', color='blue')
plt.xlabel('Date')
plt.ylabel('Sales Volume')
plt.title('Synthetic Apparel Sales Data')
plt.legend()
plt.show()

# Shows sales distribution by category in boxplot
plt.figure(figsize=(10, 5))
sns.boxplot(x=dataFrame['category'], y=dataFrame['sales_volume'])
plt.title('Sales Distribution by Category')
plt.show()