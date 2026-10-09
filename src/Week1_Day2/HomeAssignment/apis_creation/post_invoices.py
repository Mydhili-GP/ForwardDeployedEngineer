from fastapi import APIRouter
from utilis.readDataFromJson import read_data_from_json,write_data_to_json
from utilis.data_model import invoices


router = APIRouter()

@router.post("/post-invoices")
def post_invoices(invoice: invoices):
    data = read_data_from_json()
    new_invoice=invoice.model_dump()
    data.append(new_invoice)
    write_data_to_json(data)
    return new_invoice