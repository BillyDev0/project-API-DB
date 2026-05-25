import requests


url = "https://jsonplaceholder.typicode.com/posts"

data_post={
    
    'title':'belajar api',
    'body':'try to be better',
    'user_Id':1
}

res=requests.post(url,json=data_post)
if res.status_code==201:
    data=res.json()
    print('Berhasil')

    print(f'title: {data['title']}')
    print(f'user_Id: {data['user_Id']}')

else:
    print('Failed')

