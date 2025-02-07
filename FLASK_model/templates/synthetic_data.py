import numpy as np
import pandas as pd
from faker import Faker
import random

np.random.seed(42)
random.seed(42)
faker = Faker()

# Generates date range (365 days of sales)
days = pd.date_range(start='2023-01-01', end='2023-12-31')

# Trend: increasing sales over time
trend = np.linspace(100, 500, len(days))

# Seasonality: Accounts for seasonal fluctuations
seasonality = 50 * np.sin(2 * np.pi * days.dayofyear / 365)

# Generate sales by combining trend and seasonality
sales_volume = trend + seasonality
sales_volume = np.clip(sales_volume, 50, None)

# Convert to DataFrame tabular data
dataFrame = pd.DataFrame({'date': days, 'sales_volume': sales_volume})

print(dataFrame.head())