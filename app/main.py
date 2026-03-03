# app/main.py
from fastapi import FastAPI
from app.routers import customer, product, sale  # <- removed trailing comma
from app.database import Base , engine
# This MUST be called 'app'

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Smart Canteen API")

# Include routers
app.include_router(customer.router)
app.include_router(product.router)
app.include_router(sale.router)

# Optional root endpoint
@app.get("/")
def root():
    return {"message": "Smart Canteen API is running"}