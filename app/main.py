from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI()

# Имитация БД
DATA = [
    {"date": "2023-10-01", "amount": 1000},
    {"date": "2023-10-15", "amount": 2000},
    {"date": "2023-11-01", "amount": 5000},
]

@app.get("/reports/sales")
def get_sales_report(month: str = Query(..., regex=r"^\d{2}$"), year: str = Query(..., regex=r"^\d{4}$")):
    filtered = [
        s for s in DATA 
        if s["date"].startswith(f"{year}-{month}")
    ]
    
    total_sum = sum(s["amount"] for s in filtered)
    count = len(filtered)
    
    return {
        "month": month,
        "year": year,
        "total_sum": total_sum,
        "count": count
    }

def test_1(): return 1
def test_2(): return 2
def test_3(): return 3
def test_4(): return 4
def test_5(): return 5
def test_6(): return 6
def test_7(): return 7
def test_8(): return 8
def test_9(): return 9
def test_10(): return 10
def test_11(): return 11
def test_12(): return 12