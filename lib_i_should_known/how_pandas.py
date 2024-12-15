import pandas as pd
# df = pd.read_csv('d4_loot.csv')
# print(df)


test_list = [1,2,3,4]
df = pd.DataFrame(test_list, columns=['category'])
df.to_csv('output.csv')

grouped = df.groupby('category').sum()
print(grouped)