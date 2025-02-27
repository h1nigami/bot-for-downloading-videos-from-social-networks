import aiosqlite
from sqlalchemy import create_engine, Column, Integer, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Bot(Base):
    __tablename__ = 'Bot'

    token = Column(BigInteger, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'Бот {self.name}'

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    nickname = Column(String)

    def __repr__(self):
        return f'User(id={self.id}, username={self.nickname})'

class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    async def connection_open(self):
        self.session = self.Session()
    
    async def connection_close(self):
        await self.session.close()
    
    async def create_user(self, tg_id:int, nickname:str):
        await self.connection_open()
        user = User(user_id=tg_id, nickname=nickname)
        self.session.add(user)
        self.session.commit()
        await self.connection_close()
    
    async def get_user(self, tg_id:int):
        self.connection_open()
        user = await self.session.query(User).get(tg_id)
        self.connection_close()
        return user
    

        