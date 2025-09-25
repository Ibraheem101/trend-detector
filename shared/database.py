import os
import uuid
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Text, Integer, Float, Boolean, DateTime, ARRAY

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Rawpost(Base):
    __tablename__ = "raw_posts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source = Column(String(50), nullable=False)
    source_id = Column(String(255))
    content = Column(Text, nullable=False)
    author = Column(String(255))
    url = Column(Text)
    engagement_score = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True))
    scraped_at = Column(DateTime(timezone=True), server_default=func.now())
    processed = Column(Boolean, default=False)
    