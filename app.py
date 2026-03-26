from fastapi import FastAPI, HTTPException
from service import get_customer_data

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Legacy Modernization API"}

@app.get("/customers/{cust_id}")
def get_customer(cust_id: str):
    customer = get_customer_data(cust_id)

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer