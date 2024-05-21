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
new_df = df[df['item_name']=='Chicken Salad Bowl']
new_df.reset_index(drop=True)
# %%
