import pandas as pd

# Load your dataset (replace 'your_dataset.csv' with your actual data file)
df = pd.read_csv('your_dataset.csv')

# Display the first few rows of the dataset to get an overview
print("Initial data:")
print(df.head())

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values:")
print(missing_values)

# Drop rows with missing values (if needed)
# df = df.dropna()

# Fill missing values (if needed)
# df['column_name'].fillna(value, inplace=True)

# Remove duplicate rows (if needed)
# df = df.drop_duplicates()

# Perform additional data cleaning and preprocessing steps as required

# Save the cleaned dataset (replace 'cleaned_dataset.csv' with your desired file name)
# df.to_csv('cleaned_dataset.csv', index=False)

# Display the cleaned data
print("\nCleaned data:")
print(df.head())