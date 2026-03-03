# app/schemas.py
from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    email: str

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    customer_id: int
    product_id: int
    quantity: int

class SaleCreate(SaleBase):
    pass

class SaleResponse(SaleBase):
    id: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str        