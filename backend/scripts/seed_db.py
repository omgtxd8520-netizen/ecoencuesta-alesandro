import os
import csv
import asyncio
import asyncpg

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://eco_user:eco_pass@db:5432/eco_db')

async def seed(csv_path='..\\..\\data\\sample_surveys.csv'):
    conn = await asyncpg.connect(DATABASE_URL)
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            await conn.execute('''INSERT INTO surveys (respondent_name, location, score, notes) VALUES ($1, $2, $3, $4)''',
                               row.get('respondent_name'), row.get('location'), int(row.get('score')), row.get('notes'))
    await conn.close()

if __name__ == '__main__':
    asyncio.run(seed())
