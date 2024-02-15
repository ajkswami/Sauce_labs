
import pandas as pd

file_path = "C:/Users/pc/Downloads/test_data.xlsx"
df = pd.read_excel(file_path)

print(df.head())

for index, row in df.iterrows():
    cell_username = row['username']
    cell_pass_word = row['password']

    print(cell_username)
    print(cell_pass_word)





