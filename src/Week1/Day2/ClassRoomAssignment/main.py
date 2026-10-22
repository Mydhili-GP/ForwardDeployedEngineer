from fastapi import FastAPI
from Get_API_FastAPI import router as get_api_router
from Post_API import router as post_api_router

app = FastAPI()
app.include_router(get_api_router)
app.include_router(post_api_router)
