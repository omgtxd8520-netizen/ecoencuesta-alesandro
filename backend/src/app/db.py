import os
from databases import Database

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://eco_user:eco_pass@localhost:5432/eco_db')

db = Database(DATABASE_URL)

async def connect():
    await db.connect()

async def disconnect():
    await db.disconnect()
