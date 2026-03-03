from sqlalchemy.orm import Session
from .. import models, schemas


def get_sales(db: Session):
    return db.query(models.Sale).all()


def get_sale(db: Session, sale_id: int):
    return db.query(models.Sale).filter(models.Sale.id == sale_id).first()


def create_sale(db: Session, sale: schemas.SaleCreate):
    db_sale = models.Sale(
        customer_id=sale.customer_id,
        product_id=sale.product_id,
        quantity=sale.quantity
    )
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale


def update_sale(db: Session, sale_id: int, sale: schemas.SaleCreate):
    db_sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()

    if db_sale:
        db_sale.customer_id = sale.customer_id
        db_sale.product_id = sale.product_id
        db_sale.quantity = sale.quantity
        db.commit()
        db.refresh(db_sale)

    return db_sale


def delete_sale(db: Session, sale_id: int):
    db_sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()

    if db_sale:
        db.delete(db_sale)
        db.commit()

    return db_sale