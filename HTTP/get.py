import requests
import pandas as pd

url='https://jsonplaceholder.typicode.com/users'

res=requests.get(url)
data=res.json()
df=pd.json_normalize(data)

# print(df[['name','email','address.city']])

# print(df[df['address.city']=="Gwenborough"]['name'])

df_kota=df.groupby('address.city').agg({
    'name':'count'
})

print(df_kota)

