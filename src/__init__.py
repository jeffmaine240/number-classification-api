from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.route import number_router

version = "v1"

app = FastAPI(
    title="Number Classification API",
    description="An API that takes a number and returns interesting mathematical properties about it, along with a fun fact",
    version=version
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)


app.include_router(number_router, prefix="/api", tags=["number"])
