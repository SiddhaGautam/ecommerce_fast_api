#here we are implementing post request with pydantic model
from fastapi import FastAPI
from pydantic import BaseModel,Field
from dataset import data

app = FastAPI()

class postClass(BaseModel):
    name:str = Field(None,min_length=3)
    age:int  = Field(None,gt=18,lt=70)
    category:str = Field(None,description="category describes the field of the client(user)")
    
@app.post("/post/data")
def post_data(user:postClass):
    product = {
        "name":user.name,
        "age":user.age,
        "category":user.category
    }
    data.append(product)
    print(data)
    return {
        "data":user.model_dump(), "message":"created successfully"
    }