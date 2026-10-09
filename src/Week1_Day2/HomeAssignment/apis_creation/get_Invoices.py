from fastapi import APIRouter
from utilis.data_model import invoices
from utilis.readDataFromJson import read_data_from_json
router = APIRouter()

@router.get("/get-invoices")
def get_invoices():
    return read_data_from_json() 

@router.get("/get-invoices/{invoice_id}")
def get_invoice_by_id(invoice_id: int):
    data = read_data_from_json()
    for invoice in data:
        if invoice["id"] == invoice_id:
            return invoice
    return {"message": "Invoice not found"}