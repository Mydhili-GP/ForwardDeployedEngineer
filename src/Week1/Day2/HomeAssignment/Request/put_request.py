from fastapi import APIRouter
from Fetch_data_fromjson import writeData, load
from data_model import InvoiceBaseModel

router = APIRouter()

@router.put("/invoices/{invoice_id}")
def update_invoice(invoice_id: str, invoice: InvoiceBaseModel):
    data = load()
    for i, existing_invoice in enumerate(data):
        if existing_invoice.get("invoiceNumber") == invoice_id:
            updated_invoice = invoice.model_dump()
            data[i] = updated_invoice
            writeData(data)
            return {"message": "Invoice updated successfully", "invoice": updated_invoice}
    return {"message": "Invoice not found"}