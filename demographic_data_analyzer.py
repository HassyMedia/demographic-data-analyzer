import pandas as pd

# Load the dataset
file_path = 'adult.data.csv'  # Modify this path as needed
data = pd.read_csv(file_path)

# 1. Count of people by race
race_count = data['race'].value_counts()

# 2. Average age of men
average_age_men = data[data['sex'] == 'Male']['age'].mean()
