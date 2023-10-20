import sys
sys.path.append(["../"])

from pathlib import Path
from typing import Any, List, Dict, Union

from pymilvus import connections, \
    utility, FieldSchema, CollectionSchema, \
    Collection, DataType

from app.exception.custom_exception import CustomException

class VectorDB:
    "VectorDB utilities"
    def __init__(self, 
        host: str = None, 
        port: str = None, 
        embedding_size: int = None, **kwargs) -> None:
        self.host = host or "localhost"
        self.port = port or "19530"
        connections.connect("default", host=self.host, port=self.port)

        # ==== Init collection ====
        self._init_disease_info(embedding_size)
        self._init_drug_info(embedding_size)
        
    def _init_disease_info(self, embedding_size: int = 1024):
        print(utility.has_collection("disease_info"))
        if not utility.has_collection("disease_info"):
            fields = [
                FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
                FieldSchema(name="title", dtype=DataType.VARCHAR, max_length=100),
                FieldSchema(name="definition", dtype=DataType.VARCHAR, max_length=1000),
                FieldSchema(name="symptom", dtype=DataType.VARCHAR, max_length=1000),
                FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=4000),
                FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=embedding_size)
            ]
            schema = CollectionSchema(fields, "Diseases info collection")
            self.disease_info_collect = Collection("disease_info", schema, consistency_level="Strong")
        else:
            self.disease_info_collect = Collection("disease_info")
            
    def _init_drug_info(self, embedding_size: int = 1024):
        if not utility.has_collection("drug_info"):
            fields = [
                FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=100),
                FieldSchema(name="title", dtype=DataType.VARCHAR, max_length=100),
                FieldSchema(name="content", dtype=DataType.VARCHAR, max_length=4000),
                FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=embedding_size)
            ]
        
            schema = CollectionSchema(fields, "Drugs info collection")
            self.drug_info_collect = Collection("drug_info", schema, consistency_level="Strong")
        
        else:
            self.drug_info_collect = Collection("drug_info")

    async def query(self, input, search_type: str = None , search_params: dict = None):
        """Query a similar string from vectordb"""
        try:
            return "Hello World"
        except Exception as exc:
            raise CustomException(exc)
        
    async def insert(self, content: Union[Dict, List], target_db: str = None):
        """Insert new embed into `target_db`"""
        # TODO: Automatically embedding the `content`
        try:
            if isinstance(content, Dict):
                content = [content] 

            test_collection = Collection("disease_test")
            test_collection.insert(data=content)
            # if target_db == "disease_info":
            #     self.disease_info_collect.insert(content)
            # elif target_db == "drug_info":
            #     self.drug_info_collect.insert(content)
            # else:
            #     raise CustomException("Invalid `target_db`")
            return "Successfully inserted"
        except Exception as exc:
            raise CustomException(exc)
