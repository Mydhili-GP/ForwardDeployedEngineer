from fastapi import APIRouter
from data_model import InvoiceBaseModel
from Fetch_data_fromjson import writeData, load

router = APIRouter()
@router.delete("/invoices/{invoice_id}")
def delete_invoice(invoice_id: str):
    invoices = load()
    for invoice in invoices:
        if invoice.get("invoice_number") == invoice_id:
            invoices.remove(invoice)
            writeData(invoices)
            return {"message": f"Invoice with ID {invoice_id} deleted successfully."}
    return {"message": f"Invoice with ID {invoice_id} not found."}