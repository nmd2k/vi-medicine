import os
import json

import sys
import logging
from typing import Dict, Any

from fastapi import APIRouter
from fastapi.responses import JSONResponse
sys.path.append([".."])

from app.business.vectordb import VectorDB
from utils.utils import latency_benchmark

logger = logging.getLogger(__name__)
router = APIRouter(tags=["VectorDB Utils"], prefix="/vectordb")
vectordb = VectorDB()

@latency_benchmark
@router.post("/query")
async def query_db(query, search_type: str = None , search_params: Dict = None):
    try:
        result = await vectordb.query(input=query, 
                                      search_type = search_type,
                                      search_params = search_params)
        
        return JSONResponse(
            content={
                "message": "Successfully",
                "content": result
            },
            status_code=200
        )
    except Exception as exc:
        return JSONResponse(
            content={
                "message": str(exc)
            },
            status_code=500
        )
    
@latency_benchmark
@router.post("/insert")
async def embed(data: Any):
    try:
        print(data)
        vectordb = VectorDB()
        # data = data["content"]
        result = await vectordb.insert(content=data)

        return JSONResponse(
            content={
                "message": "Successfully",
                "content": result
            },
            status_code=200
        )
    except Exception as exc:
        return JSONResponse(
            content={
                "message": str(exc)
            },
            status_code=500
        )
