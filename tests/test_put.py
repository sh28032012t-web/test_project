import rest_request.put_users as get_module
from rest_request.put_users import update_user
from schemes.BD.database_test import engine_test
from schemes.model import UpdateUser
from sqlalchemy import text


get_module.engine = engine_test


def test_update_user():
    with engine_test.begin() as connection:
        result = connection.execute(
            text("""
                INSERT INTO users (first_name, last_name, age)
                VALUES (:first_name, :last_name, :age)
                RETURNING *
            """),
            {
                "first_name": "test",
                "last_name": "test",
                "age": 1
            }
        )
        
        user = result.fetchone()
        user_dict = dict(user._mapping)
    
    update_body = UpdateUser(
        first_name="updated",
        last_name="user",
        age=20
    )
    
    updated_user = update_user(
        user_dict["id"],
        update_body
    )
    
    assert updated_user["id"] == user_dict["id"]
    assert updated_user["first_name"] == "updated"
    assert updated_user["last_name"] == "user"
    assert updated_user["age"] == 20
    
    with engine_test.begin() as connection:
        result = connection.execute(
            text("""
                SELECT *
                FROM users
                WHERE id = :user_id
            """),
            {
                "user_id": user_dict["id"]
            }
        )
        
        user_test = result.fetchone()
        
        assert user_test is not None
        assert updated_user == dict(user_test._mapping)
    
    with engine_test.begin() as connection:
        connection.execute(
            text("""
                DELETE FROM users
                WHERE id = :user_id
            """),
            {
                "user_id": user_dict["id"]
            }
        )