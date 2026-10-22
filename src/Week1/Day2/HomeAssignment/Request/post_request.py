from fastapi import APIRouter
from Fetch_data_fromjson import writeData, load
from data_model import InvoiceBaseModel

router = APIRouter()

@router.post("/invoices")
def create_invoice(invoice: InvoiceBaseModel):
    data = load()
    new_invoice = invoice.model_dump()
    data.append(new_invoice)
    writeData(data)
    return {"message": "Invoice created successfully", "invoice": new_invoice}