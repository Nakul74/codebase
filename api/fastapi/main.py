from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from typing import List, Optional
import pandas as pd
from fastapi.responses import FileResponse
import redis_cache

class info_params(BaseModel):
    torrent_id: str

class Params(BaseModel):
    HSN: List[str] = Field(..., description="List of HSN code")
    title: str = Field(..., min_length=5)
    is_active: bool = True
    name: Optional[str] = None
    email: str
    password: str
    confirm_password: str
    code: int

    @validator("HSN")
    def validate_hsn(cls, value):
        for hsn in value:
            if not hsn.isdigit() or len(hsn) not in [2, 4, 6]:
                raise ValueError("HSN code must be 2, 4, or 6 digits.")
        return value
    
    @validator("confirm_password", pre=True, always=True)
    def verify_password_match(cls, value, values):
        password = values.get("password")

        if password != value:
            raise ValueError("The two passwords did not match.")
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "HSN": ["3304", "123456", "12", "12345"],
                "title": "Example Title",
                "email": "example@example.com",
                "password": "example_password",
                "confirm_password": "example_password",
                "code": 123
            }
        }

app = FastAPI(
    title='DGCIS export data web app',
    description='Given HSN code, the app will return India export data',
    version='1.0.0'
)

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])

def preprocess_list(l):
    l = l[0].split(',')
    l = [i.strip() for i in l if i.strip()]
    return list(set(l))

@app.get("/")
async def home():
    return {"message": "server is on"}

@app.post("/data/")
async def get_data(data: Params):
    try:
        data_dict = data.dict()
        return data_dict
    except Exception as e:
        print("Error in retrieving and processing data: %s", e)
        return {}

@app.post("/translate/")
def create_upload_file(
    brand_name: str = Form(...),
    receiver_email_list: List[str] = Form(...),
    file: UploadFile = File(...),):
    
    df = pd.read_csv(file.file)
    # df.to_csv('data.csv',index=False)
    receiver_email_list = preprocess_list(receiver_email_list)
    
    d = {}
    d['file'] = file.filename
    d['email_list'] = receiver_email_list
    d['brand_name'] = brand_name
    return d

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_path = file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return FileResponse(file_path, media_type="image/png")

@app.post("/info")
def get_info(data: info_params):
    torrent_id = data.torrent_id
    
    cached_data = redis_cache.get_cached_data(torrent_id)
    data = {}
    if cached_data:
        data = json.loads(cached_data)
    else:
        data = {'torrent_id':torrent_id}
        redis_cache.set_cached_data(torrent_id, json.dumps(data),expire_time=3600)

    return data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info",reload=True)