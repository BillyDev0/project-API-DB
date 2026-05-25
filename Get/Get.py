from fastapi import FastAPI

app = FastAPI()

@app.get("/halo")
def halo():
    return {'msg':'Hello Bro'}

@app.get("/items/{id}")
def get_item(id:int):
    return {'id':id}

@app.get('/{user}/{id}')
def get_data_user(user:str,id:int):
    return {"user": user,
            "id": id
            }

@app.get('/order/{user_name}/{user_id}/{order_id}')
def get_order(user_name:str,user_id:int,order_id:int):
    return {
        "user_name":user_name,
        "user_id":user_id,
        "order_id":order_id
    }

@app.get('/product/{kategory}/{item_id}')
def get_product(kategory:str,item_id:int):
    return {
        "kategory":kategory,
        "item_id":item_id
    }

@app.get('/identitas/{nama}/{kelas}/{no_absen}')
def identitas_siswa(nama:str,kelas:str,no_absen:str):
    return {
        'nama':nama,
        'kelas':kelas,
        'no_absen':no_absen
    }