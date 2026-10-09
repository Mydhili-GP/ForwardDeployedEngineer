from pydantic import BaseModel

class Invoices(BaseModel):
    id: int
    amount: float
    status: str
    nameOfCustomer: str