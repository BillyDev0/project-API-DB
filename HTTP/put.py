import requests 

url= "https://jsonplaceholder.typicode.com/posts/1"

data_put={
    'userId':2,
    'title':'Try to be better',
    'body':'Ambil resiko atau miskin selamanya, gaakan ada orang yang peduli sama lu kecuali diri lu sendiri'
}
res=requests.put(url,json=data_put)

data=res.json()

print(res.status_code)
print(data)


