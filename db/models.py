from sqlalchemy import (Boolean,Column, ForeignKey, Integer, String, Enum, Text)
from sqlalchemy.orm import relationship
from db._setup import Base


class Admin: 
    __tablename__ = "admins"
    admin_id = Column(Integer, primary_key= True)
    email = Column(String(100),unique=True, index= True, nullable= False )
    _password = Column(String(100), nullable=False)
