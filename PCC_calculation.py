import pandas as pd

# Load expression matrix with genes as rows, samples as columns
df = pd.read_csv('./data/dynamic_expression_matrix_TPM5_CV50_stem.csv', index_col=0)

# Transpose to have genes as columns for correlation calculation
df = df.T

# (Optional) Check values for genes of interest (GOIs)
goi_dict = {
    "SULTR3.2a": "PtXaTreH.08G131500",
    "SULTR3.4a": "PtXaTreH.03G041400"
}
goi = list(goi_dict.values())
print(df[goi].head())  # Visual check

# Transpose back if needed (though not required for correlation here)
# df = df.T

# Compute Pearson correlation coefficient matrix
pcc_matrix = df.corr(method='pearson')

# Save PCC matrix to file
pcc_matrix.to_csv('./data/pcc_matrix.csv')