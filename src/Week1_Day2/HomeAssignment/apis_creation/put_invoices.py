from fastapi import APIRouter, HTTPException
from utilis.readDataFromJson import read_data_from_json, write_data_to_json
from utilis.data_model import invoices

router = APIRouter()

@router.put("/put-invoices/{invoice_id}")
def put_invoices(invoice_id: int, updated_invoice: invoices):
    data = read_data_from_json()

    for item in data:
        if item["id"] == invoice_id:
            item["name"] = updated_invoice.name
            item["amount"] = updated_invoice.amount
            item["status"] = updated_invoice.status
            write_data_to_json(data)
            return item

    raise HTTPException(status_code=404, detail="Invoice not found")