from fastapi import APIRouter,HTTPException  
from utilis.readDataFromJson import read_data_from_json,write_data_to_json
from utilis.data_model import invoices

router=APIRouter()

@router.delete('/delete-invoice/{invoice_id}')
def delete_invoice(invoice_id: int):
    data = read_data_from_json()

    for item in data:
        if item["id"] == invoice_id:
            data.remove(item)
            write_data_to_json(data)
            return {"message": f"Invoice {invoice_id} deleted"}

    raise HTTPException(status_code=404, detail="Invoice not found")
