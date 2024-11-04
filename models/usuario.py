# models.py
from sqlalchemy import Column, Integer, String
from database import Base

# Modelo de Usuario
class Usuario(Base):
    __tablename__ = "usuarios" 
    id = Column(Integer, primary_key=True)  
    usuario = Column(String)  
    pasword = Column(String)
    
