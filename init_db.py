import asyncio
from sqlalchemy import text
from app.core.database import engine, Base
from app.models.domain import Document, DocumentChunk

async def init_models():
    async with engine.begin() as conn:
        print("Enabling pgvector extension...")
        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
        
        print("Creating database tables...")
        await conn.run_sync(Base.metadata.create_all)
        
    print("Database initialized successfully.")
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(init_models())