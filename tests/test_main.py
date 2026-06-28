import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def mock_data(monkeypatch):
    # Фикстура может подменять данные в БД, если это необходимо
    pass

def test_monthly_sales_report_e2e():
    # 1. Запрос данных за октябрь (10) 2023
    response = client.get("/reports/sales?month=10&year=2023")
    
    assert response.status_code == 200
    data = response.json()
    
    # 2. Проверка агрегации (сумма: 1000 + 2000 = 3000, количество: 2)
    assert data["total_sum"] == 3000
    assert data["count"] == 2
    assert data["month"] == "10"