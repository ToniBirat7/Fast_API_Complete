from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
DATABASE_URL = "sqlite+aiosqlite:///sqlite.db" # Db file location  and name

engine = create_async_engine(DATABASE_URL, echo=True) # SQL Enginer, turn off echo in production

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)