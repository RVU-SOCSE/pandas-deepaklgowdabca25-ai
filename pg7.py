import pandas as pd

# -------------------------------
# Creating a DataFrame from scratch
# -------------------------------
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)

print("DataFrame from Scratch:")
print(df)

# -------------------------------
# Adding a new column 'Bonus'
# -------------------------------
df['Bonus'] = df['Salary'] * 0.10

print("\nDataFrame after adding 'Bonus' column:")
print(df)

# -------------------------------
# Reading data from a CSV file
# -------------------------------
df = pd.read_csv(r'C:/python deepak/prog7.csv')

print("\nFirst 6 rows of the DataFrame:")
print(df.head(6))

# -------------------------------
# Display column names and data types
# -------------------------------
print("\nColumn names and data types:")
print(df.info())

# -------------------------------
# Display full DataFrame
# -------------------------------
print("\nOriginal DataFrame:")
print(df)

# -------------------------------
# Identifying missing values
# -------------------------------
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

# -------------------------------
# Filling missing values (example: 'Q1' column)
# -------------------------------
if 'Q1' in df.columns:
   df['q1'] = df['Q1'].fillna(df['Q1'].mean())
   print("\nDataFrame after filling missing values in 'Q1' column:")
   print(df)
else:
   print("\nColumn 'Q1' not found in CSV file.")
