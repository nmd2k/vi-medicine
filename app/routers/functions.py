import os
import json

import sys
import logging
from typing import List, Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse
sys.path.append([".."])

from app.business.functions import Functions
from app.exception.custom_exception import CustomException
from utils.utils import latency_benchmark

logger = logging.getLogger(__name__)
router = APIRouter(tags=["Chatmodel Utils"], prefix="/chat")

@latency_benchmark
@router.post("/generate")
async def generate(message: str, prompt: str = None):
    try:
        agent = Functions()
        result = await agent.generate(message=message, prompt=prompt)
        
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
@router.post("/embed")
async def embed(message: str):
    try:
        agent = Functions()
        result = await agent.embed(message=message)

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
