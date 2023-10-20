import time

import numpy as np
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)

fmt = "\n=== {:30} ===\n"
search_latency_fmt = "search latency = {:.4f}s"

#################################################################################
# 1. connect to Milvus
print(fmt.format("start connecting to Milvus"))
connections.connect("default", host="localhost", port="19530")

#################################################################################
# 2. create collection

if not utility.has_collection("disease_info"):
    fields = [
        FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
        FieldSchema(name="title", dtype=DataType.VARCHAR, max_length=100),
        FieldSchema(name="definition", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="symptom", dtype=DataType.VARCHAR, max_length=1000),
        FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=4000),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=2000)
    ]
    
    schema = CollectionSchema(fields, "Diseases info collection")
    disease_info_collect = Collection("disease_info", schema, consistency_level="Strong")
    print(fmt.format("create collection `disease_info`"))

if not utility.has_collection("drug_info"):
    fields = [
        FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
        FieldSchema(name="title", dtype=DataType.VARCHAR, max_length=100),
        FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=4000),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=2000)
    ]

    schema = CollectionSchema(fields, "Drugs info collection")
    drug_info_collect = Collection("drug_info", schema, consistency_level="Strong")
    print(fmt.format("create collection `drug_info`"))