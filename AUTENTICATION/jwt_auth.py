from jose import jwt,JWTError
from datetime import datetime,timedelta

SECREAT_KEY='ban8aba42ca$#2hKsnaea#na@uaba#@'
ALGORITHM='HS256'

def create_token(username):
    payload={
        'username':username,
        'exp':datetime.utcnow() + timedelta(minutes=30)
    }

    token=jwt.encode(payload,SECREAT_KEY,algorithm=ALGORITHM)
    return token


def verify_token(token):
    try:
        payload=jwt.decode(token,SECREAT_KEY,algorithms=[ALGORITHM])
        return payload['username']
    except JWTError:
        return None