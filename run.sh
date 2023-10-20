export TIKTOKEN_CACHE_DIR="/datadrive05/dungnm31/.tmp"

cd src/
uvicorn main:app --host='0.0.0.0' --port=3000 --reload --workers=4