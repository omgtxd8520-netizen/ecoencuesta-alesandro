import os
from motor.motor_asyncio import AsyncIOMotorClient
from urllib.parse import quote_plus

MONGO_URL = os.getenv('MONGO_URL', os.getenv('DATABASE_URL', 'mongodb://mongo:27017'))

# Support simple authless URL or one with credentials
client = AsyncIOMotorClient(MONGO_URL)
_db = client.get_default_database() if client.get_default_database() else client['eco_db']

async def connect():
    # motor client connects lazily; perform a ping to verify
    await client.admin.command('ping')

async def disconnect():
    client.close()

def get_db():
    return _db
