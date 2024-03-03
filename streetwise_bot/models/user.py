from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from streetwise_bot.models.base import Base


class User(Base):
    """Represents a user model."""

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    username = Column(String, nullable=True, unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
