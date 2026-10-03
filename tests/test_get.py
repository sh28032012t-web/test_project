from schemes.BD.database_test import engine_test
from rest_request.get_users import find_user
from sqlalchemy import text
from schemes.model import ResponseUser

user_id = 4

user = find_user(4)

def test_find_user():
    with engine_test.connect() as connection:
        result = connection.execute(
            text("""
                SELECT *
                FROM users
                WHERE id = :user_id
            """),
            {
                "user_id": user_id
            }
        )
        user_test = result.fetchone()
        
        assert user == ResponseUser(
            id=user_test.id,
            first_name=user_test.first_name,
            last_name=user_test.last_name,
            age=user_test.age,
        )