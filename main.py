import pandas as pd
 

file_path = r"C:\Users\canid\OneDrive\Masaüstü\Python\CS_178\project\cs178_ml\db\diabetic_data.csv"
df = pd.read_csv(file_path, sep=",", encoding="utf-8", na_values=["?", "NA"])   #creates dataframe

print(df.info)
