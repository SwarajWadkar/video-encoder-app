import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from app.models import Base

# ✅ Direct connection string (no settings.py needed)
DATABASE_URL = "postgresql://user:password@db:5432/videos"

# ✅ SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# ✅ Create tables with retry (waits for DB to be ready)
def init_db(retries: int = 10, delay: int = 2):
    for i in range(retries):
        try:
            Base.metadata.create_all(bind=engine)
            print("✅ Database connected and tables created.")
            return
        except OperationalError as e:
            print(f"⏳ DB not ready (attempt {i+1}/{retries}): {e}")
            time.sleep(delay)
    raise Exception("❌ Failed to connect to the database after multiple attempts.")
