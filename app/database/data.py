
connected_clients = set()
order_db = dict()

# INITIAL DATA FOR TESTING
order_db[672] = {
    "id": 672,
    "stocks": "TEST-DATA-1",
    "quantity": 150,
    "status": "EXECUTED"
    }
order_db[383] = {
    "id": 383,
    "stocks": "TEST-DATA-2",
    "quantity": 350,
    "status": "PENDING"
}
order_db[188] = {
    "id": 188,
    "stocks": "TEST-DATA-3",
    "quantity": 999,
    "status": "CANCELLED"
}

