from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.session import Base

# Base Model for user creation
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    user_email = Column(String, unique=True, index=True)
    user_password = Column(String, nullable=False)

# Base model for file upload
class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    owner_id = Column(Integer, ForeignKey("users.user_id"))
