from database import customers_db

def get_customer_data(cust_id):
    data = customers_db.get(cust_id)

    if not data:
        return None

    # simulate COBOL logic (decode status)
    status_map = {
        "A": "ACTIVE",
        "C": "CLOSED"
    }

    return {
        "customerId": cust_id,
        "name": data["name"],
        "balance": data["balance"],
        "status": status_map.get(data["status"], "UNKNOWN")
    }