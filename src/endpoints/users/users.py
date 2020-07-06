from fastapi.routing import APIRouter

from models.user import User, UserIn_Pydantic, User_Pydantic

router = APIRouter()


@router.get('/user/', tags=['users'])
async def register_user(id: int) -> User_Pydantic:
    return await User_Pydantic.from_tortoise_orm(await User.get(id=id))


@router.post('/user/', tags=['users'])
async def create_user(user: UserIn_Pydantic):
    user = await User.create(**user.dict())
    return user
