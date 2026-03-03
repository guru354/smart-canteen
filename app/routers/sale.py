from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..crud import sale as crud
from .. import schemas

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/", response_model=schemas.SaleResponse)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.create_sale(db, sale)


@router.get("/", response_model=list[schemas.SaleResponse])
def read_sales(db: Session = Depends(get_db)):
    return crud.get_sales(db)


@router.get("/{sale_id}", response_model=schemas.SaleResponse)
def read_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = crud.get_sale(db, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale


@router.put("/{sale_id}", response_model=schemas.SaleResponse)
def update_sale(sale_id: int, sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    updated_sale = crud.update_sale(db, sale_id, sale)
    if not updated_sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return updated_sale


@router.delete("/{sale_id}", response_model=schemas.SaleResponse)
def delete_sale(sale_id: int, db: Session = Depends(get_db)):
    deleted_sale = crud.delete_sale(db, sale_id)
    if not deleted_sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return deleted_sale