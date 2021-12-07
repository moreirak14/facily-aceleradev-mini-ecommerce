import jwt, bcrypt
from datetime import datetime, timedelta
from app.repositories.users_repository import UsersRepository
from fastapi import Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import ExpiredSignatureError


oauth2_schema = OAuth2PasswordBearer(tokenUrl='/auth/login')


JWT_SECRET = 'FASD5FASG33FDWCV7FSADG8FD9ADFA'
ALGORITHM = 'HS256'


def create_token(data: dict, expire_delta = None):
    payload = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta # --> pega a data agora e soma com expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60) # --> ou... por padrão será 60 min

    payload.update({'exp': expire})

    return jwt.encode(payload, JWT_SECRET, ALGORITHM) # --> modelo de criptografia HASH 256


def authenticate(user_repository: UsersRepository = Depends(), 
          form_data: OAuth2PasswordRequestForm = Depends()):
    user = user_repository.find_by_email(form_data.username)

    """ Valida se há usuario """
    if not user:
        return False

    """ Valida se o hash informado é o mesmo que está cadastrado no banco """
    if not bcrypt.checkpw(form_data.password.encode('utf8'), user.password):
        return False

    return create_token({'id': user.id})


def get_user(token: str = Depends(oauth2_schema), 
             user_repository: UsersRepository = Depends()):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=ALGORITHM)
        user = user_repository.get_by_id(payload['id'])
        return user
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='This token has expired')


def only_admin(user = Depends(get_user)):
    if not user.role == 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Allowed only for admin')
