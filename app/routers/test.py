import os
import json

import sys
import logging
import random
from typing import Dict, List

from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse
sys.path.append([".."])


logger = logging.getLogger(__name__)
router = APIRouter(tags=["For Test Only"], prefix="/test")


SYMPTOM = """Giai đoạn rét run: rét run toàn thân, môi tái, nổi da gà. Giai đoạn rét run kéo dài khoảng 30 phút - 2 giờ. [1]
Giai đoạn sốt nóng: rét run giảm, bệnh nhân thấy nóng dần, thân nhiệt có thể tới 400C - 410C, mặt đỏ, da khô nóng, mạch nhanh, thở nhanh, đau đầu, khát nước, có thể hơi đau tức vùng gan lách. Giai đoạn sốt nóng kéo dài khoảng 1-3 giờ. [2]
Giai đoạn vã mồ hôi: thân nhiệt giảm nhanh, vã mồ hôi, khát nước, giảm nhức đầu, mạch bình thường, bệnh nhân cảm thấy dễ chịu.
Cơn sốt thể cụt: sốt không thành cơn, chỉ thấy rét run, kéo dài khoảng 1-2 giờ. Thể sốt này hay gặp ở những bệnh nhân đã nhiễm sốt rét nhiều năm.
Thể ký sinh trùng lạnh (người lành mang trùng): xét nghiệm máu có ký sinh trùng nhưng không bị sốt, vẫn sinh hoạt và lao động bình thường. Thể này thường gặp ở vùng sốt rét lưu hành nặng."""

class Symptom(BaseModel):
    symptom: str
    user_info: str = None

@router.post("/diagnose")
def test_diagnose(symptoms: Symptom):
    print(symptoms)
    
    try:
        assert type(symptoms.symptom) == str
        result = dict(diagnosis="Bệnh sốt rét",
                    explain=SYMPTOM,
                    source=["https://www.vinmec.com/vi/benh/sot-ret-4443/",
                            "https://www.vinmec.com/vi/tin-tuc/thong-tin-suc-khoe/suc-khoe-tong-quat/cac-thuoc-dieu-tri-benh-sot-ret/"]
                    )
        
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

class Disease(BaseModel):
    name: str
    user_info: str = None
    
class Medicine(BaseModel):
    name: str

@router.post("/check_medicine")
async def check_medicine(medicine: Medicine, disease: Disease):
    print(medicine)
    print(disease)
    try:
        result = random.choice(["RELEVANT", "IRRELEVANT", "UNDEFINED"])
        explain = random.choice(["Paracetamol phù hợp để điều trị bệnh, xét với thể trạng bệnh nhân và triệu chứng đang gặp phải.", "Nước tiểu chuột không phù hợp với bệnh nhân. Đây là một chất có hại và không nên sử dụng.", "Một lời cầu nguyện cần xem xét thêm. Vì mặc dù không có vấn đề gì, nhưng bác sĩ nên xem xét lại thuốc này."])
        print(result)
        return JSONResponse(
            content={
                "message": "Successfully",
                "content": dict(review=result, explain=explain)
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
    print(disease)
    try:
        result = random.choice(["Paracetamol", "Quinine"])
        explain = random.choice(["Paracetamol phù hợp để điều trị bệnh, xét với thể trạng bệnh nhân và triệu chứng đang gặp phải.", "Nước tiểu chuột không phù hợp với bệnh nhân. Đây là một chất có hại và không nên sử dụng.", "Một lời cầu nguyện cần xem xét thêm. Vì mặc dù không có vấn đề gì, nhưng bác sĩ nên xem xét lại thuốc này."])
        return JSONResponse(
            content={
                "message": "Successfully",
                "content": dict(suggestion=result, explain=explain)
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
    print(medicines)
    try:
        result = []
        for i in range(len(medicines) - 1):
            for j in range(i + 1, len(medicines)):
                result.append(dict(source=medicines[i].name, target=medicines[j].name))
        
        for item in result:
            item["compatibility"] = random.choice(["RELEVANT", "IRRELEVANT", "UNDEFINED"])
            item["explain"] = "Hai loại thuốc này bla bla..."
                
        print(result)
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

@router.post("/internal_fail_test")
async def internal(s):
    try:
        raise Exception("(Intention) Internal Server Error")
    except Exception as exc:
        return JSONResponse(
            content={
                "message": str(exc)
            },
            status_code=500
        )
