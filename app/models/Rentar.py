from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Renta(Base):
    __tablename__ = 'rentar'

    idRenta = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime, default=datetime.now)
    dias_de_renta = Column(Integer)
    estatus = Column(Integer)

    usuario = relationship("Usuario")
    pelicula = relationship("Pelicula")

    def __repr__(self):
        return f"<Renta(idRenta={self.idRenta}, idUsuario={self.idUsuario}, idPelicula={self.idPelicula}, fecha_renta={self.fecha_renta}, estatus={self.estatus})>"
