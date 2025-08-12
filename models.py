from sqlalchemy import Column, Integer, String, Float, Date, DateTime, DECIMAL
from sqlalchemy.sql import func
from database import Base

class Hotel(Base):
    __tablename__ = "hoteles"
    id = Column(Integer, primary_key=True, index=True)
    ciudad = Column(String(50), unique=True, nullable=False)
    direccion = Column(String(100))

class Habitacion(Base):
    __tablename__ = "habitaciones"
    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, nullable=False)
    tipo = Column(String(20), nullable=False)
    capacidad_maxima = Column(Integer, nullable=False)
    cantidad = Column(Integer, nullable=False)

class Tarifa(Base):
    __tablename__ = "tarifas"
    id = Column(Integer, primary_key=True, index=True)
    ciudad = Column(String(50), nullable=False)
    tipo_habitacion = Column(String(20), nullable=False)
    temporada = Column(String(10), nullable=False)
    precio_por_persona = Column(DECIMAL(10,2), nullable=False)

class Reserva(Base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True)
    ciudad = Column(String(50), nullable=False)
    tipo_habitacion = Column(String(20), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    personas = Column(Integer, nullable=False)
    habitaciones_reservadas = Column(Integer, nullable=False)
    total_a_pagar = Column(DECIMAL(10,2), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())