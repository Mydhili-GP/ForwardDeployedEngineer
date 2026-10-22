from pydantic import BaseModel

class InvoiceBaseModel(BaseModel):
    id: int
    amount: float
    status: str