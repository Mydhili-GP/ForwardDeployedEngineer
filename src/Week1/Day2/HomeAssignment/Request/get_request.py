from fastapi import APIRouter, HTTPException
from  data_model import InvoiceBaseModel
from Fetch_data_fromjson import load

router = APIRouter()

@router.get("/get_request")
def get_request():
    return load()

@router.get("/get_request/{invoice_id}")
def get_request_by_id(invoice_id: str):
    data = load()
    for invoice in data:
        if invoice["invoiceNumber"] == invoice_id:
            return invoice
    raise HTTPException(status_code=404, detail="Invoice not found")
