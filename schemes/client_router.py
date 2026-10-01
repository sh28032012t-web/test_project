from fastapi.testclient import TestClient
from schemes.config import app

client = TestClient(app)