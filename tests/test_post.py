import rest_request.post_users as get_module
from rest_request.post_users import create_user
from fastapi.testclient import TestClient
from schemes.BD.database_test import engine_test
from schemes.config import app
from schemes.model import CreateUser
from sqlalchemy import text

client = TestClient(app)

get_module.engine = engine_test

user_body = CreateUser(
    first_name="test",
    last_name="test",
    age=1
)

user = create_user(user_body)

def test_create_user():
    with engine_test.begin() as connection:
        result = connection.execute(
            text("""
                SELECT *
                FROM users
                WHERE id = :user_id
            """),
            {
                "user_id": user["id"]
            }
        )
        user_test = result.fetchone()
        
        assert user_test is not None
        assert user == dict(user_test._mapping)
        
        with engine_test.begin() as connection:
            result = connection.execute(
                text("""
                    DELETE FROM users
                    WHERE id = :user_id
                """),
                {
                    "user_id": user["id"]
                }
            )