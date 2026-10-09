from pydantic import BaseModel

class invoices(BaseModel):
    id: int
    name: str
    amount: float   
    status: str