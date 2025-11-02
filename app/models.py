from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import String
from app.db import engine

class Base(AsyncAttrs, DeclarativeBase):
  pass

class User(Base):
  __tablename__ = "user"

  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)
  email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)

# Function to create the Table
async def create_table():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)