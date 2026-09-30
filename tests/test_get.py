from schemes.BD.database_test import engine_test
from rest_request.get_users import find_user
from sqlalchemy import text

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
        test_user = result.fetchone()
        
        assert user == dict(test_user._mapping)