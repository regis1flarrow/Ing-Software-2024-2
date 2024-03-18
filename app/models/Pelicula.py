from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pelicula(Base):
    __tablename__ = 'peliculas'

    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String)
    genero = Column(String)
    duracion = Column(Integer)
    inventario = Column(Integer)

    def __repr__(self):
        return f"<Pelicula(idPelicula={self.idPelicula}, nombre={self.nombre}, genero={self.genero}, inventario={self.inventario})>"
