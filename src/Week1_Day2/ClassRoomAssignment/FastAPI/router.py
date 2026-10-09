from fastapi import FastAPI
from Learning_post_api import router as postAPI
from Learnring_get_api import router as getAPI

app= FastAPI()
app.include_router(postAPI)  
app.include_router(getAPI)