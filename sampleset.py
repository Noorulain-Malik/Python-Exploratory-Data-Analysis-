# sampleset.py
import pandas as pd
import shutil

def load_and_clean_data():
    # List of columns you want to read
    usecols = ['loan_amnt', 'funded_amnt', 'funded_amnt_inv', 'int_rate', 'purpose', 'title','loan_status']

    # Define the source file path
    source_file = "C:\\Users\\noora\\OneDrive\\Desktop\\Project python\\Lending_club.py\\loan.csv"

    # Define the destination file path
    destination_file = "C:\\Users\\noora\\OneDrive\\Desktop\\Project python\\Lending_club.py\\loan_copy.csv"

    # Copy the file
    shutil.copy(source_file, destination_file)

    # Read the CSV file with specified columns
    df = pd.read_csv(destination_file, usecols=usecols)

    # Capitalize the first word of the column names
    df.columns = df.columns.str.capitalize()

    # Handling missing values
    df.dropna(inplace=True)

    # Removing duplicates
    df.drop_duplicates(inplace=True)

    # Handling outliers (example: cap loan amount at 99th percentile)
    loan_amnt_99 = df['Loan_amnt'].quantile(0.99)
    df = df[df['Loan_amnt'] < loan_amnt_99]

    # Standardizing text data
    df['Purpose'] = df['Purpose'].str.lower()

    # Correcting typos (example)
    df['Purpose'].replace({'debtconsolidation': 'debt_consolidation'}, inplace=True)

    # Encoding categorical variables
    df['Purpose'] = df['Purpose'].astype('category').cat.codes

    # Scaling numerical features
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    df[['Loan_amnt', 'Funded_amnt', 'Funded_amnt_inv', 'Int_rate']] = scaler.fit_transform(df[['Loan_amnt', 'Funded_amnt', 'Funded_amnt_inv', 'Int_rate']])

    return df
