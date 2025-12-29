from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Используем asyncpg как драйвер для асинхронного взаимодействия с PostgreSQL
SQLALCHEMY_DATABASE_URL = 'postgresql+asyncpg://postgres:password123@172.30.30.19:5430/react'

# Создаем асинхронный движок с использованием asyncpg
engineasync = create_async_engine(SQLALCHEMY_DATABASE_URL,
        echo=False,
        pool_size=50,  # Максимальное количество постоянных соединений в пуле
        max_overflow=20,  # Максимальное количество дополнительных соединений сверх pool_size
        pool_timeout=30,  # Время ожидания в секундах, прежде чем выдать ошибку, если все соединения заняты
        pool_recycle=1800,  # Переподключение через каждые 30 минут для обновления соединений
        pool_pre_ping=True,  # Проверка "живости" соединения перед его использованием
        future=True # Отключение кэширования на уровне движка
    )

# Создаем асинхронный sessionmaker
async_session = sessionmaker(
    engineasync, expire_on_commit=False, class_=AsyncSession
)

# Функция для получения асинхронной сессии базы данных
async def get_db_async():
    async with async_session() as session:
        yield session