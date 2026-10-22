from pydantic import BaseModel

class InvoiceBaseModel(BaseModel):
    invoice_number: str
    date: str
    paymentStatus: str
    name: str