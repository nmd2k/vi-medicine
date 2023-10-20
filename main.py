import os
import uvicorn
from fastapi import FastAPI, APIRouter

import pymilvus
    
from fastapi.middleware.cors import CORSMiddleware
from app.routers.suggestion import router as suggestion_router
from app.routers.functions import router as functions_router
# from app.routers.vectordb import router as vectordb_router
from app.routers.test import router as test_router

app = FastAPI()

origins = str(os.environ.get("CORS_ALLOW_ORIGINS")).split(",") if os.environ.get("CORS_ALLOW_ORIGINS") else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    pass

# Configure a router
router = APIRouter(prefix="/api/v1")
router.include_router(suggestion_router)
router.include_router(functions_router)
# router.include_router(vectordb_router)
router.include_router(test_router)

app.include_router(router)

uvicorn.Config(app, log_level="debug", access_log=True)