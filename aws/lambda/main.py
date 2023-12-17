from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,Field
from typing import List
from mangum import Mangum

class params(BaseModel):
    HSN: List[str] = Field(..., description="List of HSN code")
    class Config:
        schema_extra = {
            "example": {
                "HSN": ["3301"]
            }
        }
    
app = FastAPI(title='UN comtrade data web app',
              description='Given HS code app will return export or import data',
              version = '1.0.0')

handler = Mangum(app)

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])

@app.get("/")
async def home():
    return {"message": "server is on"}

@app.post("/data")
async def get_data(data: params):
    data = data.dict()
    return data