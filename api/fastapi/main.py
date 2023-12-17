from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from typing import List, Optional

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

@app.get("/")
async def home():
    return {"message": "server is on"}

@app.post("/data")
async def get_data(data: Params):
    try:
        data_dict = data.dict()
        return data_dict
    except Exception as e:
        print("Error in retrieving and processing data: %s", e)
        return {}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info",reload=True)