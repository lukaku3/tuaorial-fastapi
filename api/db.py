from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "demo")
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "dbpassword")
MYSQL_HOST = os.environ.get("MYSQL_HOST", "db")
MYSQL_PORT = os.environ.get("MYSQL_PORT", "3306")
MYSQL_CHARSET = os.environ.get("MYSQL_CHARSET", "utf8mb4")
MYSQL_ALLOW_EMPTY_PASSWORD = os.environ.get("MYSQL_ALLOW_EMPTY_PASSWORD", 1)
# ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"
ASYNC_DB_URL = f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset={MYSQL_CHARSET}"


async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()


async def get_db():
    async with async_session() as session:
        yield session
