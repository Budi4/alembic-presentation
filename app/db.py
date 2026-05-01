import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg2://alembic_demo:alembic_demo@db:5432/alembic_demo",
)


class Base(DeclarativeBase):
    pass


engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
