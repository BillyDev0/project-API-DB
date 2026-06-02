from jose import jwt,JWTError
from datetime import timedelta,datetime

SECREATE_KEY='sj8a7sbjalkew23vf'
ALGORITHM='HS256'

def create_token(username:str):
    payload={
        'username':username,
        'exp':datetime.utcnow() + timedelta(minutes=50)
    }

    token=jwt.encode(payload,SECREATE_KEY,algorithm=ALGORITHM)
    return token


def verify_token(token):
    try:
        payload=jwt.decode(token,SECREATE_KEY,algorithms=[ALGORITHM])
        return payload['username']
    except JWTError:
        return None
    
