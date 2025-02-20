from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_process_text():
    response = client.post("/process-text/", json={"text": "This is a sample document about science."})
    assert response.status_code == 200
    assert "dominant_topic" in response.json()

def test_process_pdf():
    with open("./data/sample.pdf", "rb") as pdf_file:
        response = client.post("/process-pdf/", files={"file": pdf_file})
    assert response.status_code == 200
    assert "dominant_topic" in response.json()
