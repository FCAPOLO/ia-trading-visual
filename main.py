from fastapi import FastAPI, UploadFile
from analysis import analyze_market

app = FastAPI()

@app.get("/")
def root():
    return {"status":"OK","message":"Backend activo"}

@app.post("/analyze")
async def analyze(file: UploadFile):
    image_bytes = await file.read()
    return analyze_market(image_bytes)
