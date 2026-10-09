from fastapi import APIRouter
from data_store import invoices

router = APIRouter()
# app = FastAPI()
# invoices = [{"id": 1, "amount": 100.0,"status": "paid", "nameOfCustomer": "John Doe"},
#                  {"id": 2, "amount": 200.0, "status": "unpaid", "nameOfCustomer": "Jane Smith"},
#                    {"id": 3, "amount": 150.0, "status": "paid", "nameOfCustomer": "Bob Johnson"}]
@router.get("/get_invoices")
def get_invoices():
    return invoices

@router.get("/get_invoices/{invoice_id}")
def get_invoice(invoice_id: int): 
    for invoice in invoices:
        if invoice["id"] == invoice_id:
            return invoice
    return {"error": "Invoice not found"}
    