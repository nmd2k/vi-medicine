# ViMedicine: An LLMs agent for drug and illness suggestion

<video src='https://github.com/user-attachments/assets/07828877-0567-40ac-b40f-0e3e37d949fd' width=180/>
Product Demonstration

## Introduction
In this project, we present a medicine agent for Vietnamese medical suggestion. 
The medicine agent can:
1. Predict illness based on patient's symptoms
2. Suggest medicine based on disease
3. Check specific medicine's suitability based on disease and patient's symptoms
4. Predict medicines' side effects or interact or violate patient's medical record

We use OpenAI GPT-3.5 model to read documents and generate medical entities, but the agent flow is not restricted to OpenAI GPT model or to Vietnamese medical domain.

> ⚠️ Notes: The full document is comming soon. 

## Install requirement
Input your chat model key in `config/.env` file.
Install via `pip`:
```bash
pip install -r <requirements.txt>
```

## Initualize Milvus server and deploy API
**Initualize milvus server and create collection**
```bash
docker-compose up -d
python setup_milvus.py
```
Notes: for the data, check out [Here](https://github.com/nmd2k/vi-medicine/releases/tag/data_v1)

**Deploy API server**
```bash
uvicorn main:app  --reload --port=<port> --workers=<n_worker>
```

## Acknowledge
This is a research project, so we do not guarantee the accuracy of the model.
Since the performance heavily depends on database (in vector store) quality, the current model precision might not meet the expectation for production use.

# Citation
```
@misc{vimedicine,
  author = {Tran Tuan Anh, Phan Quang Hung, Dung Manh Nguyen},
  title = {ViMedicine: An Vietnamese LLMs agent for drug and illness suggestion},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/nmd2k/vi-medicine/}},
}
```

**Our team:**
- Tran Tuan Anh*
- Phan Quang Hung*
- Dung Manh Nguyen*

*: Equals contribution
