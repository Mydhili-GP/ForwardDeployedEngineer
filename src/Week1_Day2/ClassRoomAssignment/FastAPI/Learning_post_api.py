from fastapi    import APIRouter
from data_model import Invoices
from data_store import invoices

router = APIRouter()
# app = FastAPI()

@router.post("/invoices")
def create_invoice(invoice: Invoices):
        new_invoice = invoice.model_dump()
        invoices.append(new_invoice)
        return new_invoice