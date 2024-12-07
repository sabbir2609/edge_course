# generate a synthetic dataset

import pandas as pd
import random
import faker

# Set a seed for reproducibility
random.seed(42)

# Create a Faker instance for generating random countries
fake = faker.Faker()

# Generate the data
data = []

countries = ['USA', 'Canada', 'UK', 'India', 'Germany', 'Australia', 'France', 'Japan', 'Brazil', 'China']
num_entries = 10  # Number of rows to generate

for _ in range(num_entries):
    country = random.choice(countries)
    age = random.randint(18, 70)  # Random age between 18 and 70
    salary = random.randint(30000, 999999)  # Random salary in the range 30k to 999k
    purchase = random.choice([True, False])  # Random purchase boolean
    
    data.append([country, age, salary, purchase])

# Create DataFrame
df = pd.DataFrame(data, columns=['Country', 'Age', 'Salary', 'Purchase'])

# Show the first few rows of the dataframe
print(df.head())

# Optionally, save to a CSV file
df.to_csv('synthetic_data.csv', index=False)
