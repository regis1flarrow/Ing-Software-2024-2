from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String)
    apPat = Column(String)
    apMat = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    superUser = Column(Boolean)

    def __repr__(self):
        return f"<Usuario(idUsuario={self.idUsuario}, nombre={self.nombre}, email={self.email}, superUser={self.superUser})>"
