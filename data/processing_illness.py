import json
import requests
from tqdm import tqdm
import pandas as pd
import numpy as np

from concurrent.futures import ThreadPoolExecutor, as_completed

GENERATE_URL = "http://4.193.50.237:3000/api/v1/chat/generate"
EMBED_URL = "http://4.193.50.237:3000/api/v1/chat/embed"

import requests

def embed(string):
    payload = {
        "message": string,
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", EMBED_URL, headers=headers, params=payload)
    return response.json()["content"]


def summary_symptom(index, symptoms_free):
    prompt = """
    Bác sĩ sẽ cung cấp thông tin về một loại bệnh.
    Việc của bạn là tóm tắt thông tin về triệu chứng của bệnh đó.
    Yêu cầu của tóm tắt là không làm mất thông tin cần thiết.
    """
    
    message = f"Thông tin bệnh:\n{symptoms_free}\nTóm tắt triệu chứng bệnh:\n"
    # print(message)
    payload = {
        "message": message,
        "prompt": prompt
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", GENERATE_URL, headers=headers, params=payload)
    return dict(id=index, summary=response.json()["content"])


path = "./Illness.json"
data = json.load(open(path, "r"))

df = pd.DataFrame(data)

symptoms_free = {}
for index, row in tqdm(df.iterrows()):
    if row["symptoms_free"]:
        symptoms_free[index] = row["symptoms_free"]
    elif row["causes"]:
        symptoms_free[index] = row["causes"]
        
summary_symptoms = []

with tqdm(total=len(symptoms_free)) as pbar:
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(summary_symptom, index=index, symptoms_free=symptoms) for index, symptoms in list(symptoms_free.items())]
        for future in as_completed(futures):
            summary_symptoms.append(future.result())
            pbar.update(1)
            
symp_df = pd.DataFrame(summary_symptoms)
new_df = df.merge(symp_df, on="id", how="left")
new_df.to_csv("./illness.csv")
