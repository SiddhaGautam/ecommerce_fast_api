#here we are implementing post request with pydantic model
from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

class postClass(BaseModel):
    name:str = Field()