import rest_request.delete_users as get_module
from rest_request.delete_users import delete_user
from schemes.client_router import client
from schemes.BD.database_test import engine_test
from sqlalchemy import text
from schemes.model import DeleteUser
from schemes.model import ResponseUser

get_module.engine = engine_test

user_body = DeleteUser(
    first_name="test",
    last_name="test",
    age=1
)

def test_remove_user():
    with engine_test.begin() as connection:
        result = connection.execute(
            text("""
                INSERT INTO users (first_name, last_name, age)
                VALUES (:first_name, :last_name, :age)
                RETURNING *
            """),
            {
                "first_name": user_body.first_name,
                "last_name": user_body.last_name,
                "age": user_body.age
            }
        )
        user = result.fetchone()
        
        dict_user = ResponseUser(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            age=user.age,
        )
        
    delete_users = delete_user(dict_user.id)
    
    assert delete_users is None