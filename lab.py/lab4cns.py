# ================================
# Dimensionality Reduction using PCA
# ================================

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Create sample dataset
data = pd.DataFrame({
    'Age': [22, 25, 47, 52, 46, 56, 55],
    'Salary': [25000, 27000, 52000, 58000, 50000, 60000, 62000],
    'Experience': [1, 2, 10, 15, 9, 18, 20]
})

print("Original Dataset:")
print(data)

# -------------------------------
# Step 1: Standardize the Data
# -------------------------------
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# -------------------------------
# Step 2: Apply PCA
# -------------------------------
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

# Convert PCA result to DataFrame
pca_df = pd.DataFrame(pca_data, columns=['PC1', 'PC2'])

print("\nPCA Reduced Dataset:")
print(pca_df)

# -------------------------------
# Step 3: Explained Variance
# -------------------------------
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)
