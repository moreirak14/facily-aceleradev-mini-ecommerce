from fastapi import APIRouter, HTTPException, status, Depends
from .schemas import ShowUserAuthenticationSchema
from app.models.models import User
from app.services.auth_service import authenticate, get_user


router = APIRouter()


@router.get('/me', response_model=ShowUserAuthenticationSchema)
def index(user: User = Depends(get_user)):
    return user


@router.post('/login')
def login(token: str = Depends(authenticate)):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='These credentials are invalid')

    return {'access_token': token, 'token_type': 'bearer'}
