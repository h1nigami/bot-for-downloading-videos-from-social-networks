import aiosqlite

class DB():
    def __init__(self, file_name):
        self.file_name = file_name

    async def connect(self):
        self.connection = await aiosqlite.connect(self.file_name)
        self.cursor = await self.connection.cursor()

    async def create_table(self):
        await self.connect()
        query = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, nickname TEXT, is_admin INTEGER DEFAULT 0)'
        await self.cursor.execute(query)
        await self.close()

    async def create_user(self, tg_id: int, nickname: str):
        await self.connect()
        query = 'INSERT INTO users (id, nickname) VALUES (?, ?)'
        await self.cursor.execute(query, (tg_id, nickname))
        await self.connection.commit()  
        await self.close()

    async def close(self):
        await self.cursor.close()
        await self.connection.close()

    async def execute(self, query, *args):
        await self.cursor.execute(query, args)
        await self.connection.commit()

    async def fetchall(self, query, *args):
        await self.cursor.execute(query, args)
        return await self.cursor.fetchall()

    async def fetchone(self, query, *args):
        await self.cursor.execute(query, args)
        return await self.cursor.fetchone()


db = DB('db.sqlite3')