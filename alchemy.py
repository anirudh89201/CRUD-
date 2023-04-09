from sqlalchemy import create_engine,Column,Integer,String,TIMESTAMP;
from sqlalchemy.orm import sessionmaker;
from sqlalchemy.ext.declarative import declarative_base;
from sqlalchemy.sql import func
engine = create_engine("postgresql://postgres:Anirudh@localhost:5432/FastAPI");
Session = sessionmaker(bind=engine);
Base = declarative_base();
class User_cred(Base):
    __tablename__ = "sqlalchemy";
    id = Column(Integer,primary_key=True,nullable=False);
    Name = Column(String,primary_key = False,nullable = False);
    Content = Column(String,primary_key=False,nullable = False);
class Create(Base):
    __tablename__ = "Users";
    email = Column(String,primary_key=False,nullable=False,unique=True);
    password = Column(String,primary_key=False,nullable=False);
    id = Column(Integer,primary_key=True,nullable=False);
    created_at = Column(TIMESTAMP(timezone=True),server_default = func.now())
    