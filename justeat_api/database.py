from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+asyncmy://gholi_pour__:2024data_Wee%25159159gholipour%25$%@p3nlmysql165plsk.secureserver.net/ph15928026353_"

engine = create_async_engine(DB_URL, echo=True, future=True)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

# Dependency to get a session
async def get_db():
    async with SessionLocal() as session:
        yield session