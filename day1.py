#문제 1 ~ 19
#20240520

import pandas as pd

# url = "https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv"
# df = pd.read_csv(url, sep='\t')
#문제1
#print(df)

#문제2
#print(df.head(5))

#문제3
# print(len(df.columns))
# print(len(df))

#문제4
#print(df.columns)

#문제4
#print(df.columns[5])

#문제5
#print(df.columns[5])

#문제6
#print(df.iloc[:,5].dtype)

url = "https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv"
df = pd.read_csv(url, encoding="EUC-KR")
#문제9
#print(df)

#문제10
#print(df.tail(3))

'''못 푼 문제'''
#문제11
#ans = df.select_dtypes(exclude=object).columns
#print(ans)

#문제12
# ans = df.select_dtypes(include=object).columns
# print(ans)

#문제13
#print(df.isnull().sum())

'''못푼문제'''
#문제14
#print(df.info())

#문제15
#print(df.describe())

#문제16
#print(df['거주인구'])

#문제17
# v_data = df['평균 속도']
# q3 = v_data.quantile(0.75)
# q1 = v_data.quantile(0.25)

# iqr = q3 - q1
# print(iqr)

'''못 푼 문제'''
#문제18
print(df['읍면동명'].nunique())

#문제 19
print(df["읍면동명"].unique())