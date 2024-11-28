from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from src.books.models import Book
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker


asyn_engine = AsyncEngine(
    create_engine(
        url=Config.DATABASE_URL_REMOTE,
        echo=True
    )
)

async def init_db():
    async with asyn_engine.begin() as conn:

        await conn.run_sync(SQLModel.metadata.create_all)
        

async def get_session() -> AsyncSession:

    Session = sessionmaker(
        bind=asyn_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session