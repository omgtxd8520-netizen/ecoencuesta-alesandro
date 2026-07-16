import os
import csv
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.getenv('MONGO_URL', os.getenv('DATABASE_URL', 'mongodb://mongo:27017'))

async def seed(csv_path='/app/data/sample_surveys.csv'):
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.get_default_database() or client['eco_db']
    docs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['score'] = int(row.get('score') or 0)
            docs.append(row)
    if docs:
        await db.surveys.insert_many(docs)
    await client.close()

if __name__ == '__main__':
    asyncio.run(seed())
