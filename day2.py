#%%
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
#%%
import pandas as pd
DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'
df = pd.read_csv(DataUrl)
# %%
#문제 21
print(df[df['quantity']==3].head(5))
# %%
#문제 22
'''못 푼 문제'''
sorted_df = df.sort_index()
print(sorted_df[sorted_df['quantity']==3].reset_index(drop=True).head(5))
# %%
#문제 23
'''못 푼 문제'''
new_df = df[['quantity', 'item_price']]
print(new_df)
# %%
#문제 24
df['new_price'] = df['item_price'].str[1:].astype('float')
# %%
#문제 25
print(df[df['new_price']<=5])
print(len(df[df['new_price']<=5]))
# %%
#문제 26
new_df = df[df['item_name']=='Chicken Salad Bowl']
new_df.reset_index(drop=True)
# %%
#문제 27
new_df = df[(df['item_name']=='Chicken Salad Bowl') & (df['new_price']<=9)]
print(new_df)
# %%
#문제 28
new_df = df.sort_values(by='new_price').reset_index(drop=True)
print(new_df)
# %%
'''못 푼 문제'''
#문제 29
new_df = df.loc[df.item_name.str.contains('Chips')]
print(new_df)
# %%
'''못 푼 문제'''
#문제 30
df.iloc[:,::2]
# %%
#문제 31
new_df = df.sort_values(by='new_price', ascending=False).reset_index(drop=True)
print(new_df)
# %%
#문제 32
'''못 푼 문제'''
Ans = df.loc[(df.item_name =='Steak Salad') | (df.item_name =='Bowl')]
print(Ans)
# %%
#문제 33
new_df = df.loc[(df.item_name == 'Steak Salad') | (df.item_name == 'Bowl')]
new_df.drop_duplicates(subset='item_name', keep='first')
# %%
#문제 34
new_df = df.loc[(df.item_name == 'Steak Salad') | (df.item_name == 'Bowl')]
new_df.drop_duplicates(subset='item_name', keep='last')
# %%
#문제 35
mean = df['new_price'].mean()
print(df[df['new_price']>=mean])
# %%
#문제 36
df.replace(to_replace='Izze', value='Fizzy Lizzy')
# %%
#문제 37
df['choice_description'].isna().sum()
# %%
#문제 38
'''못 푼 문제'''
import numpy as np
df.replace(to_replace=np.NaN, value='Nodata')
# %%
#문제 39
df[df.choice_description.str.contains("Black", na=False)]
# %%
#문제 40
total = len(df.choice_description)
Veg = df[df.choice_description.str.contains("Vegetables", na=False)]
length = len(Veg)
print(total-length)
# %%
#문제 41
df[df.item_name.str.startswith('N')]
# %%
#문제 42
df[df.item_name.str.len() >= 15]
# %%
