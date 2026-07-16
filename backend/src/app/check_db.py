import os
import asyncio
import asyncpg

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://eco_user:eco_pass@localhost:5432/eco_db')

async def check():
    conn = await asyncpg.connect(DATABASE_URL)
    row = await conn.fetchrow('SELECT COUNT(*) AS cnt FROM surveys')
    await conn.close()
    print(f"surveys_count={row['cnt']}")

if __name__ == '__main__':
    asyncio.run(check())
