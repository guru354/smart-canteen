from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import customer as crud
from .. import schemas
from ..database import get_db

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post("/", response_model=schemas.CustomerResponse)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@router.get("/", response_model=list[schemas.CustomerResponse])
def read_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db)

@router.get("/{customer_id}", response_model=schemas.CustomerResponse)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{customer_id}", response_model=schemas.CustomerResponse)
def update_customer(customer_id: int, customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    updated_customer = crud.update_customer(db, customer_id, customer)
    if not updated_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer

@router.delete("/{customer_id}", response_model=schemas.CustomerResponse)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    deleted_customer = crud.delete_customer(db, customer_id)
    if not deleted_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return deleted_customer