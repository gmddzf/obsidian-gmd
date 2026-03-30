import pandas as pd
df=pd.read_csv('D:\Ai_Study\date/movies_sample.csv')
print("前5行数据:")
print(df.head(5))
print("\n" + "="*50 + "\n")
first_10=df.iloc[0:10]
print(first_10)