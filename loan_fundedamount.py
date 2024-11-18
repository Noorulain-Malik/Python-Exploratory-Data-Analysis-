
import matplotlib.pyplot as plt
import seaborn as sns
import random
import sampleset

# Load and clean the data
df = sampleset.load_and_clean_data()

# Use the random module to generate a random sample from the cleaned dataset
sample_size = 1000  # Adjust the sample size as needed
random_state = random.randint(0, 10000)  # Generate a random seed
random_sample = df.sample(n=sample_size, random_state=random_state)  # Get a random sample using the random seed
print(random_sample.head())

# Plotting the two graphs side by side

# Setup the figure and axes
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

# First plot: Loan amount applied by borrower
sns.histplot(random_sample['Loan_amnt'], bins=20, ax=axes[0], kde=True, color='blue')
axes[0].set_title('Distribution of Loan Amount Applied by Borrower')
axes[0].set_xlabel('Loan Amount Applied')
axes[0].set_ylabel('Frequency')

# Second plot: Loan amount funded
sns.histplot(random_sample['Funded_amnt'], bins=20, ax=axes[1], kde=True, color='green')
axes[1].set_title('Distribution of Loan Amount Funded')
axes[1].set_xlabel('Loan Amount Funded')
axes[1].set_ylabel('Frequency')

# Adjust layout
plt.tight_layout()
plt.show()
