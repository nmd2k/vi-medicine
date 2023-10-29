import os
import json

import sys
import logging
from typing import List, Optional

from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
sys.path.append([".."])

from app.business.suggestion import MedicineAgent
from app.exception.custom_exception import CustomException
from utils.utils import latency_benchmark

logger = logging.getLogger(__name__)
router = APIRouter(tags=["Medicine Suggestion"], prefix="/dev")

class Disease(BaseModel):
    name: str
    user_info: str = None
    
class Medicine(BaseModel):
    name: str

class Symptom(BaseModel):
    symptom: str
    user_info: str = None

@latency_benchmark
@router.post("/diagnose")
async def diagnose(symptoms: Symptom):
    try:
        assert type(symptoms.symptom) == str
        agent = MedicineAgent()
        result = await agent.diagnose(symptoms=symptoms)
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

@router.post("/check_medicine")
async def check_medicine(medicine: Medicine, disease: Disease):
    try:
        agent = MedicineAgent()
        result = await agent.check_medicine(medicine=medicine,
                                            disease=disease)
        
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

@router.post("/suggest_medicine")
async def suggest_medicine(disease: Disease, listed: List[Medicine] = None):
    try:
        agent = MedicineAgent()
        result = await agent.suggest_medicine(disease=disease, listed=listed)
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
    

@router.post("/compatible_calculator")
async def compatible_calculator(medicines: List[Medicine]):
    try:
        agent = MedicineAgent()
        result = await agent.compatible_calculator(medicines)
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
