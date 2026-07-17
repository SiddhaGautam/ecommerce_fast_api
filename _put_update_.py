from fastapi import FastAPI,status,Response
from pydantic import BaseModel,Field
from dataset import data

app = FastAPI()

class postClass(BaseModel):
     name:str = Field(None,min_length=3)
     age:int  = Field(None,gt=18,lt=70)
     category:str = Field(None,description="category describes the field of the client(user)")

@app.put("/update/{info}")
def update_data(info:str,user_data:postClass,response:Response):
     #first check weather the record is available or not in the data
     for user in data:
          if user["name"] == info:
               user["name"] = user_data.name
               user["age"] = user_data.age
               user["category"] = user_data.category
               return {"data":user,"message":"updated succesfully"}

     return {"message":"no user found"}