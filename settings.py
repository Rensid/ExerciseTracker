from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import redis
from config import REDIS_HOST

REFRESH_TOKEN_EXPIRE_DAYS = 7
ACCESS_TOKEN_EXPIRE_HOURS = 12

redis_client = redis.StrictRedis(
    host=f'{REDIS_HOST}', port=6379, db=0, decode_responses=True)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
