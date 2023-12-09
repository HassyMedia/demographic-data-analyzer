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

# 6. Minimum hours per week
min_hours_per_week = data['hours-per-week'].min()

# 7. Percentage of people working minimum hours per week earning >50K
perc_min_hours_more_than_50K = (data[(data['hours-per-week'] == min_hours_per_week) & (data['salary'] == '>50K')]).shape[0] / data[data['hours-per-week'] == min_hours_per_week].shape[0] * 100

# 8. Country with highest percentage of people earning >50K
country_salary_counts = data.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
highest_earning_country, highest_earning_country_perc = country_salary_counts['>50K'].idxmax(), country_salary_counts['>50K'].max() * 100

# 9. Most popular occupation for those who earn >50K in India
top_occupation_india = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]['occupation'].mode()[0]

# Print the results
print("Race Count:\n", race_count)
print("\nAverage Age of Men:", average_age_men)
print("\nPercentage of People with a Bachelor's Degree:", bachelors_deg)
print("\nPercentage of People with Advanced Education Earning More Than 50K:", perc_adv_edu_more_than_50K)
print("\nPercentage of People Without Advanced Education Earning More Than 50K:", perc_no_adv_edu_more_than_50K)
print("\nMinimum Hours per Week:", min_hours_per_week)
print("\nPercentage of People Working Minimum Hours per Week Earning More Than 50K:", perc_min_hours_more_than_50K)
print("\nCountry with the Highest Percentage of People Earning More Than 50K:", highest_earning_country, "with", highest_earning_country_perc, "%")
print("\nMost Popular Occupation for Those Who Earn More Than 50K in India:", top_occupation_india)


