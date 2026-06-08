from jose import jwt,JWTError
from datetime import datetime,timedelta

SECREATE_KEY='1s9Hf6shw'
ALGORITHM='HS256'

def create_token(username):
    payload={
        'username':username,
        'exp':datetime.utcnow() + timedelta(hours=1)
    }

    token=jwt.encode(payload,SECREATE_KEY,algorithm=ALGORITHM)
    return token

def verifikasi_token(token):
    try:
        payload=jwt.decode(token,SECREATE_KEY,algorithms=[ALGORITHM])
        return payload['username']
    except JWTError:
        return None