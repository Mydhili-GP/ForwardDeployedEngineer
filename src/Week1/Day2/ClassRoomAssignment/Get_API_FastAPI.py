from fastapi import APIRouter
from Models import InvoiceBaseModel
from Data_Store import invoices

router = APIRouter()


@router.get("/get-invoices")
def get_invoices():
    return invoices

@router.get("/get-invoice/{invoice_id}")
def get_invoice(invoice_id: int):
    for invoice in invoices:
        if invoice["id"] == invoice_id:
            return invoice
    return {"error": "Invoice not found"}