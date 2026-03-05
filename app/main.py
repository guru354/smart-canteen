from fastapi import FastAPI

from .database import engine
from . import models


from .routers import customer
from .routers import product
from .routers import sale


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Smart Canteen API")



app.include_router(customer.router)
app.include_router(product.router)
app.include_router(sale.router)


@app.get("/")
def root():
    return {"message": "Smart Canteen API Running"}