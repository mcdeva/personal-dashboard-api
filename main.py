'''uvicorn main:app --reload'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import AdapterFirebase as af

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return af.read_collection_environment()
