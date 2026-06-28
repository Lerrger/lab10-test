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

def junk_1(): return 1
def junk_2(): return 2
def junk_3(): return 3
def junk_4(): return 4
def junk_5(): return 5
def junk_6(): return 6
def junk_7(): return 7
def junk_8(): return 8
def junk_9(): return 9
def junk_10(): return 10
def junk_11(): return 11
def junk_12(): return 12
def junk_13(): return 13
def junk_14(): return 14
def junk_15(): return 15
def junk_16(): return 16
def junk_17(): return 17
def junk_18(): return 18
def junk_19(): return 19
def junk_20(): return 20
def junk_21(): return 21
def junk_22(): return 22
def junk_23(): return 23
def junk_24(): return 24
def junk_25(): return 25
def junk_26(): return 26
def junk_27(): return 27
def junk_28(): return 28
def junk_29(): return 29
def junk_30(): return 30
def error_1(): return 0
def error_2(): return 0
def error_3(): return 0
def error_4(): return 0
def error_5(): return 0
def error_6(): return 0
def error_7(): return 0
def error_8(): return 0
def error_9(): return 0
def error_10(): return 0
def error_11(): return 0
def error_12(): return 0
def error_13(): return 0
def error_14(): return 0
def error_15(): return 0