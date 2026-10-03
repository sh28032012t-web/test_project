from fastapi.testclient import TestClient
from schemes.api_app import app

client = TestClient(app)