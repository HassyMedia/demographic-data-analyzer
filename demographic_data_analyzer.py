import pandas as pd

# Load the dataset
file_path = 'adult.data.csv'  # Modify this path as needed
data = pd.read_csv(file_path)

# 1. Count of people by race
race_count = data['race'].value_counts()

# 2. Average age of men
average_age_men = data[data['sex'] == 'Male']['age'].mean()

# 3. Percentage of people with a Bachelor's degree
bachelors_deg = (data['education'] == 'Bachelors').mean() * 100

# 4. Percentage of people with advanced education (Bachelors, Masters, Doctorate) earning >50K
advanced_edu = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
perc_adv_edu_more_than_50K = (data[advanced_edu & (data['salary'] == '>50K')]).shape[0] / data[advanced_edu].shape[0] * 100

# 5. Percentage of people without advanced education earning >50K
perc_no_adv_edu_more_than_50K = (data[~advanced_edu & (data['salary'] == '>50K')]).shape[0] / data[~advanced_edu].shape[0] * 100
