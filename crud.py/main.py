import json
import requests

url='https://jsonplaceholder.typicode.com/posts'
res=requests.get(url)
data_siswa=res.json()

def write(data):
   with open('data.json','w') as f:
      json.dump(data,f,indent=1)

def load():
   with open('data.json') as f:
      return json.load(f)

def menu():
   print('''=== MENU ===
1. lihat data
2. tambah data
3. update data
4. hapus data''')
   return int(input('Pilih: '))

def main():
   write(data_siswa)
   data=load()

   while True:
      pilihan_menu=menu()
      if pilihan_menu==1:
         id=int(input('masukan id: '))
         for item in data:
            if id == item['id']:
               print(f'userId: {item['userId']}')
               print(f'title: {item['title']}')
               print(f'body: {item['body']}')
               return
         else:
            print('id tidak tersedia')



      elif pilihan_menu==2:
         userId=int(input('Masukan userId: '))
         id=int(input('Masukan id: '))
         title=input('Masukan title: ')
         body=input('Masukan body: ')

         data_post={
            'userId':userId,
            'id':id,
            'title':title,
            'body':body
         }
         res=requests.post(url,json=data_post)
         if res.status_code==201:
            data=res.json()
            print('Berhasil ditambah')
         else:
            print('Gagal ditambah')


      elif pilihan_menu==3:
         userId=int(input('Masukan userId: '))
         id=int(input('Masukan id: '))
         title=input('Masukan title: ')
         body=input('Masukan body: ')
   
         data_put={
            'userId':userId,
            'id':id,
            'title':title,
            'body':body
         }

         res=requests.put(url,json=data_put)
         print(res.status_code)
         print(res.url)
         # print(res.status_code)

         # if res.status_code==200:
         #    data=res.json()
         #    print('Data berhasil diperbarui')
         # else:
         #    print('Data gagal diperbarui')

      write(data)
main()




    




       

