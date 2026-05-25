import requests

url = "https://jsonplaceholder.typicode.com/posts/4"

res=requests.delete(url)

if res.status_code==200:
    print('Berhasil dihapus')

else:
    print('Gagal')