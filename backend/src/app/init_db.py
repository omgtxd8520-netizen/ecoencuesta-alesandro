import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv('MONGO_URL', os.getenv('DATABASE_URL', 'mongodb://mongo:27017'))

async def init():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.get_default_database() or client['eco_db']
    # Ensure collection and index
    await db.create_collection('surveys') if 'surveys' not in await db.list_collection_names() else None
    await db.surveys.create_index('created_at')
    await client.close()

if __name__ == '__main__':
    asyncio.run(init())
