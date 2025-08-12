from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router
import database, models


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="API de Reservas Hoteleras")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Bienvenido al sistema de reservas de hoteles"}