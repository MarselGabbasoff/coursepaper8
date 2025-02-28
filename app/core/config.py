import os

from dotenv import load_dotenv

load_dotenv()
SALT = os.getenv("SALT")
MONGODB_URI = os.getenv("MONGODB_URI")
TTL_INDEX_SECONDS = os.getenv("TTL_INDEX_SECONDS")
DATABASE_NAME = os.getenv("DATABASE_NAME")
TEST_DATABASE_NAME = os.getenv("TEST_DATABASE_NAME")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")