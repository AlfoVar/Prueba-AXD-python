# Sistema de Reservas Hotelera - Prueba Técnica

Este proyecto implementa una solución full-stack para la gestión de disponibilidad y tarifas de una cadena hotelera, permitiendo a los usuarios consultar habitaciones disponibles, calcular precios según temporada y tipo de alojamiento, y visualizar resultados en tiempo real.

La solución es completamente **dockerizada**, lo que garantiza portabilidad y ejecución consistente en cualquier entorno.

---

## Tecnologías Utilizadas

### Frontend
- **Angular 17** (standalone components, signals)
- **TypeScript**
- **Reactive Forms** (validación en tiempo real)
- **HttpClient** (comunicación con API)
- **Nginx** (servidor ligero y proxy inverso)

### Backend
- **Python 3.11**
- **FastAPI** (framework moderno para APIs REST)
- **SQLAlchemy** (ORM para PostgreSQL)
- **Pydantic** (modelos y validación de datos)
- **Uvicorn** (servidor ASGI de alto rendimiento)

### Base de Datos
- **PostgreSQL 15** (almacenamiento relacional)
- Esquema relacional con integridad referencial

### DevOps
- **Docker** (contenerización)
- **Docker Compose** (orquestación de servicios)
- **Nginx** (proxy inverso para evitar CORS)

---

## Arquitectura del Sistema

La arquitectura sigue un diseño en capas claro y escalable:

<img width="1680" height="1050" alt="Image" src="https://github.com/user-attachments/assets/cd97cea8-877e-442e-80ca-e65d6d53ee24" />

Todos los servicios están orquestados mediante `docker-compose`, lo que permite desplegar toda la aplicación con un solo comando.

---

## Modelo de Base de Datos

El modelo relacional está compuesto por las siguientes tablas:

| Tabla | Descripción |
|------|-------------|
| `hoteles` | Información de cada sede (ciudad, dirección) |
| `habitaciones` | Tipos de habitación por hotel (estándar, premium, VIP), capacidad y cantidad |
| `tarifas` | Precios por persona según ciudad, tipo de habitación y temporada (alta/baja) |
| `reservas` | Registros de reservas existentes (fechas, personas, habitaciones) |

### Relaciones

- `hoteles` → `habitaciones`: **Uno a muchos** (un hotel tiene múltiples tipos de habitaciones).
- `reservas` → `hoteles` y `habitaciones`: Relación lógica por `ciudad` y `tipo_habitacion`.
- `tarifas` → `hoteles`: Relación por ciudad para aplicar precios dinámicos.

> **Nota**: Se usa `ciudad` como campo categórico en `reservas` y `tarifas` para simplificar consultas y evitar joins complejos, manteniendo claridad en una prueba técnica.

---

## 🐳 Ejecución con Docker

Este proyecto está completamente dockerizado. Para ejecutarlo:


