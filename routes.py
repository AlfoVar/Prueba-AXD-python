from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func  
from datetime import date
from pydantic import BaseModel

import database, models, schemas

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def es_temporada_alta(fecha: date) -> bool:
    mes = fecha.month
    return mes in [6, 7, 8] or (mes == 12) or (mes == 1)

class DisponibilidadRequest(BaseModel):
    ciudad: str
    fecha_inicio: date
    fecha_fin: date
    personas: int
    tipo_habitacion: str | None = None

@router.post("/disponibilidad", response_model=list[schemas.ResultadoBusqueda])
def buscar_disponibilidad(
    req: DisponibilidadRequest,
    db: Session = Depends(get_db)
):
    ciudad = req.ciudad
    fecha_inicio = req.fecha_inicio
    fecha_fin = req.fecha_fin
    personas = req.personas
    tipo_habitacion = req.tipo_habitacion
    # 1. Obtener habitaciones del hotel
    hotel = db.query(models.Hotel).filter(models.Hotel.ciudad == ciudad).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")

    habitaciones_db = db.query(models.Habitacion).filter(models.Habitacion.hotel_id == hotel.id)
    if tipo_habitacion:
        habitaciones_db = habitaciones_db.filter(models.Habitacion.tipo == tipo_habitacion)
    habitaciones_db = habitaciones_db.all()

    resultados = []

    for hab in habitaciones_db:
        if personas > hab.capacidad_maxima:
            continue 

        ocupadas = db.query(func.sum(models.Reserva.habitaciones_reservadas)) \
            .filter(models.Reserva.ciudad == ciudad) \
            .filter(models.Reserva.tipo_habitacion == hab.tipo) \
            .filter(models.Reserva.fecha_inicio < fecha_fin) \
            .filter(models.Reserva.fecha_fin > fecha_inicio) \
            .scalar() or 0

        disponibles = hab.cantidad - ocupadas
        if disponibles <= 0:
            continue

        temporada = "alta" if es_temporada_alta(fecha_inicio) else "baja"
        tarifa = db.query(models.Tarifa).filter(
            models.Tarifa.ciudad == ciudad,
            models.Tarifa.tipo_habitacion == hab.tipo,
            models.Tarifa.temporada == temporada
        ).first()

        precio_por_persona = tarifa.precio_por_persona if tarifa else 100.000
        total = precio_por_persona * personas

        resultados.append({
            "ciudad": ciudad,
            "tipo_habitacion": hab.tipo,
            "habitaciones_disponibles": disponibles,
            "tarifa_por_persona": float(precio_por_persona),
            "tarifa_total": total
        })

    return resultados