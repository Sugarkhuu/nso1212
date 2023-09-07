import pandas as pd 



fn = 'files/1617547220953.xls'
df = pd.read_excel(fn)
df = df.fillna(method='ffill')
df = df.fillna(method='ffill', axis=1)
try: 
    num_ind = df[df.iloc[:,0]=='№'].index
except:
    num_ind = df[df.iloc[:,1]=='№'].index

df = df.iloc[num_ind[0]:]


df['name'] = df[df.columns[1]] + df[df.columns[2]] 
df = df.drop(df.columns[[0, 1, 2]], axis=1)

new_columns = df.iloc[0:2].astype(str).apply(' '.join, axis=0)
df.columns = new_columns
# Remove rows 2 and 3
# df.to_csv('result/result1.csv', encoding='utf-8-sig')
df = df.drop([2, 3])
# Reset the index if needed
df.reset_index(drop=True, inplace=True)

df.to_csv('result/result1.csv', encoding='utf-8-sig')

