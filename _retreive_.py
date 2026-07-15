from fastapi import FastAPI,Query

#create a local database
data = [
    {"name":"gautam tiwari","age":21,"category":"student"},
    {"name":"siddharth","age":23,"category":"employee"},

]
app = FastAPI()
# @app.get("/home")
# def get_all_data():
#     return {"data":data,"total":len(data)}

@app.get("/home")
def get_all_queried_data(queries:str|None):
    filtered = data
    for item in filtered:
        if(item["category"]== queries):
            return {"data":item}
    return {"message":"no such record found"}
