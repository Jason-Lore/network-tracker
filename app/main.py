import asyncio
from fastapi import FastAPI

from app.routes import sites, devices
from app.services.ping import ping_loop

app = FastAPI()

app.include_router(sites.router)
app.include_router(devices.router)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(ping_loop())


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    return {"status": "ok"}