from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas
from ..crud.product import (
    create_product as crud_create_product,
    get_product as crud_get_product,
    get_products as crud_get_products,
    update_product as crud_update_product,
    delete_product as crud_delete_product,
)
from ..database import get_db

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud_create_product(db, product)


@router.get("/", response_model=list[schemas.ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return crud_get_products(db)


@router.get("/{product_id}", response_model=schemas.ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = crud_get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated_product = crud_update_product(db, product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete("/{product_id}", response_model=schemas.ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = crud_delete_product(db, product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product