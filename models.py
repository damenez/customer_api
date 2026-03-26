from pydantic import BaseModel

class Customer(BaseModel):
    customerId: str
    name: str
    balance: float
    status: str