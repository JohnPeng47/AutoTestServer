from datetime import datetime, timedelta
import jwt
from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import pytz

from .schema import User, JWTData, UserAuthRequest
from .utils import jwt_decode
from .exceptions import DuplicateUserException
from .config import ACCESS_TOKEN_EXPIRE_DAYS

from src.database.db import DBConnection
from src.database.exceptions import MongoUnacknowledgeError

from logging import getLogger

logger = getLogger("base")
db_conn = DBConnection()

# Change this to use secrets manager at some point
SECRET_KEY = "gangster_lean_boogie"
ALGORITHM = "HS256"

def create_user(user: UserAuthRequest) -> User:
    res = db_conn.get_collection("users").insert_one(user.dict())

    # IDK about this exception
    if not res.acknowledged:
        raise MongoUnacknowledgeError("User creation Unacknowledged")

    return User(**user.dict())

def delete_user(user: User) -> User:
    res = db_conn.get_collection("users").delete_one(user.dict())

    if not res.acknowledged:
        raise MongoUnacknowledgeError("User deletion Unacknowledged")

    return True
    

def get_user_by_id(authReq: UserAuthRequest) -> User | None:
    user_dict = db_conn.get_collection("users").find_one({
        "id": authReq.id
    })

    if user_dict:
        return User(**user_dict)

    return None

def get_email_from_user(user: UserAuthRequest) -> str:
    return user.email

def get_user_by_email(email: str = Depends(get_email_from_user)) -> User | None:
    user_dict = db_conn.get_collection("users").find_one({
        "email": email
    })

    if user_dict:
        return User(**user_dict)

    return None

def user_email_checker(user: User) -> bool | None:
    user_exists = get_user_by_email(user.email)

    return True if user_exists else False

def create_access_token(email: str):
    """
    Utility function to create a new access token with expiration.
    """
    # need to convert to local timezone
    local_tz = pytz.timezone('US/Eastern')
    local_now = datetime.now(local_tz)

    expire = local_now + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode = {
        "email": email,
        "exp": expire
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# probably should make this depend on another dependency to retrieve the user


def validate_token(authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer())) -> JWTData:
    """
    Validate the JWT token from the request's Authorization header.
    """
    token = authorization.credentials
    try:
        payload = jwt_decode(token)
        # payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload

    # expiration is automatically checked during decode
    except jwt.ExpiredSignatureError:
        user = payload.get("email")
        logger.debug(f"Token for user {user} has expired")
        raise HTTPException(status_code=401, detail="Invalid token")

    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

# TODO: replace decoded_token with JWTData
# IMPORTANT: this is our main session implementation


def get_user_from_token(decoded_token: JWTData = Depends(validate_token)) -> User:
    """
    Extract the username from the decoded JWT token.
    """
    # Extracting username from the decoded token
    email = decoded_token.email

    if not email:
        raise HTTPException(
            status_code=400, detail="Email not present in the token"
        )

    user = get_user_by_email(email)
    if not user:
        raise HTTPException(
            status_code=400, detail="Not a registered user"
        )

    return user
