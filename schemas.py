from pydantic import BaseModel
from datetime import date

class ResultadoBusqueda(BaseModel):
    ciudad: str
    tipo_habitacion: str
    habitaciones_disponibles: int
    tarifa_por_persona: float
    tarifa_total: float

class Config:
    from_attributes = True