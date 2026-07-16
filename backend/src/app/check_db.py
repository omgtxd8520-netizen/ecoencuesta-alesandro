import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv('MONGO_URL', os.getenv('DATABASE_URL', 'mongodb://mongo:27017'))

async def check():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.get_default_database() or client['eco_db']
    cnt = await db.surveys.count_documents({})
    await client.close()
    print(f"surveys_count={cnt}")

if __name__ == '__main__':
    asyncio.run(check())
