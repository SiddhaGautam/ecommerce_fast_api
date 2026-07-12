from fastapi import FastAPI
app = FastAPI()

#so @ is used for the decorator
@app.get("/")
def home():
    return ("this is our home page:)")
