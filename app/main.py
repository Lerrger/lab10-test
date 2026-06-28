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

def junk_logic(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"

def another_untested_function():
    for i in range(10):
        print(f"Junk line {i}")
    return True