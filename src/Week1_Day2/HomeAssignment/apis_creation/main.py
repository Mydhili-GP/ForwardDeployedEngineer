from fastapi import FastAPI
from get_Invoices import router as getAPi
from post_invoices import router as postAPi
from put_invoices import router as putAPi
from delete_invoices import router as deleteAPi

app= FastAPI()
app.include_router(getAPi)
app.include_router(postAPi)
app.include_router(putAPi)
app.include_router(deleteAPi)  
