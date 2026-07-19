#crud operations for cart shopping
from fastapi import FastAPI ,status,responses
from pydantic import BaseModel,Field

app = FastAPI()
cart = []
class checkPost(BaseModel):
    userId:int = Field(None, description="unique id of the user")
    address:str = Field(None,description="location of the user")
    productId:int = Field(None,description="unique product id")
    itemCount:int = Field(None,description="total item in the cart of a specific product id")
    totalCount:int = Field(None,description="total count of the product")
    isempty:bool = Field(False,description="to check the avalability of the product")
#to fetch all the products in the cart
@app.get("/")
def viewProducts():
    return {"cart_products":cart}

#to add the items in the cart
@app.post("/products")
def addProducts(product:checkPost):
    if product.isEmpty:
        return {"message":"not available"}
    for pid in product.productId:
        
    

#to checkout the cart details
@app.post("/products/checkout")
def checkoutProducts():