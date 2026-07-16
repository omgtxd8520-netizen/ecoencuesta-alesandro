import os
import asyncio
import asyncpg

async def init():
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://eco_user:eco_pass@db:5432/eco_db')
    conn = await asyncpg.connect(DATABASE_URL)
    sql = open(__file__.replace('init_db.py', 'models.py')).read()
    await conn.execute(sql)
    await conn.close()

if __name__ == '__main__':
    asyncio.run(init())
