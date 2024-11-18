import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import datetime as dt
import shutil
import warnings
warnings.filterwarnings("ignore")#to ignore warnings


#Loading the dataset and converting into dataframe



# List of columns you want to read
usecols = ['loan_amnt', 'funded_amnt', 'funded_amnt_inv', 'int_rate','purpose','title']  # Update this list based on actual columns


# Define the source file path
source_file = "C:\\Users\\noora\\OneDrive\\Desktop\\Project python\\Lending_club.py\\loan.csv"

# Define the destination file path
destination_file = ("C:\\Users\\noora\\OneDrive\\Desktop\\Project python\\Lending_club.py\\loan_copy.csv")

# Copy the file
shutil.copy(source_file, destination_file)

print(f"File copied from {source_file} to {destination_file}")
# Read the CSV file with specified columns
df = pd.read_csv(destination_file, usecols=usecols)

# Capilize the first word of the column name
                                                                #DATA CLEANING                      
df.columns = df.columns.str.capitalize()
print(df.head()) #to see the first 5 rows of the dataset
print(df.shape)#to see the number of rows and columns in the dataset (2260668, 6)
print(df.dropna(inplace=True))              #Remove all rows with null values (2237342, 6)
print(df.head)
print(df.shape)
#calculating maximum and minimum loan amount and funded amount

print("max loan amount " + str(df['Loan_amnt'].max()))
print("Min loan amount  "+ str(df['Loan_amnt'].min()))
print("funded loan amount "+ str(df['Funded_amnt'].max()))
print("min funded amount " + str(df['Funded_amnt'].min()))

                                                                    # max loan amount 40000
                                                                    # Min loan amount  500
                                                                    # funded loan amount 40000
                                                                    # min funded amount 500
print(df.drop_duplicates(inplace = True))   #No duplicate values found 


                                            # count the number of loan amounts for each purpose
purpose_count = df['Purpose'].value_counts()
print(purpose_count)                                             
                                                #     Purpose
                                                # debt_consolidation    255997
                                                # credit_card           117259
                                                # home_improvement       45273
                                                # other                  43588
                                                # major_purchase         22199
                                                # small_business         14946
                                                # medical                13217
                                                # car                    13155
                                                # moving                  8383
                                                # house                   8367
                                                # vacation                7523
                                                # wedding                 2311
                                                # renewable_energy        1298
                                                # educational              421
                                            #Plotting graph for loan amount and purpose
colors = ['green','red','blue','yellow','orange','purple','pink','gray','brown','cyan','magenta'] 
df['Purpose'].value_counts().plot(kind='bar',color=colors[:len(purpose_count)])
plt.xlabel('Purpose')
plt.ylabel('Count')
plt.title('Number of Loans for Each Purpose')
plt.show()
