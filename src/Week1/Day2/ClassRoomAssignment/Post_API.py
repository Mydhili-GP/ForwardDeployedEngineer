from fastapi import APIRouter
from Models import InvoiceBaseModel
from Data_Store import invoices

router = APIRouter()

@router.post("/Create-invoices")
def create_invoice(invoice: InvoiceBaseModel):
    invoices.append(invoice.model_dump())
    return {"message": "Invoice created successfully", "invoice": invoice}