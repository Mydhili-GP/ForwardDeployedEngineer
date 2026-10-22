from fastapi import FastAPI
from Request.get_request import router as get_router
from Request.post_request import router as post_router
from Request.put_request import router as put_router
from Request.delete_request import router as delete_router

app = FastAPI()
app.include_router(get_router)
app.include_router(post_router) 
app.include_router(put_router)
app.include_router(delete_router)