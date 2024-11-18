import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import datetime as dt
import warnings

warnings.filterwarnings("ignore")  # to ignore warnings

# Correct syntax for usecols
df = pd.read_csv("loan.csv", usecols=["loan_status"])
print(df.head())  # Print the first few rows to check if the data is loaded correctly

# Define what constitutes a 'bad loan'
bad_loan_statuses = ['Charged Off', 'Default', 'Late (31-120 Days)', 'In Grace Period']

# Convert loan_status column to title case to match bad_loan_statuses
df['loan_status'] = df['loan_status'].str.title()

# Calculate the number of bad loans
bad_loans = df[df['loan_status'].isin(bad_loan_statuses)]
num_bad_loans = bad_loans.shape[0]

# Calculate the number of good loans
num_total_loans = df.shape[0]
num_good_loans = num_total_loans - num_bad_loans

# Calculate percentages
bad_loan_percentage = (num_bad_loans / num_total_loans) * 100
good_loan_percentage = 100 - bad_loan_percentage

# Prepare data for the pie chart
sizes = [bad_loan_percentage, good_loan_percentage]
labels = ['Bad Loans', 'Good Loans']
colors = ['yellow', 'blue']

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Percentage of Bad Loans vs Good Loans')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

# Show the plot
plt.show()
