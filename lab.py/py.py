# ================================
# Feature Transformation
# ================================

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

# Create sample dataset
data = pd.DataFrame({
    'Age': [22, 25, 47, 52, 46, 56, 55],
    'Salary': [25000, 27000, 52000, 58000, 50000, 60000, 62000],
    'Experience': [1, 2, 10, 15, 9, 18, 20],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance', 'IT']
})

print("Original Dataset:")
print(data)

# -------------------------------
# 1. Create New Feature
# -------------------------------
data['Salary_per_Experience'] = data['Salary'] / data['Experience']
print("\nAfter Creating New Feature:")
print(data)

# -------------------------------
# 2. One Hot Encoding (FIXED)
# -------------------------------
encoder = OneHotEncoder(sparse_output=False)
encoded_data = encoder.fit_transform(data[['Department']])

encoded_df = pd.DataFrame(
    encoded_data,
    columns=encoder.get_feature_names_out(['Department'])
)

data_encoded = pd.concat(
    [data.drop('Department', axis=1), encoded_df],
    axis=1
)

print("\nAfter One Hot Encoding:")
print(data_encoded)

# -------------------------------
# 3. Normalization
# -------------------------------
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data_encoded)

normalized_df = pd.DataFrame(
    normalized_data,
    columns=data_encoded.columns
)

print("\nAfter Normalization:")
print(normalized_df)
