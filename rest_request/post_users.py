from schemes.BD.database import engine
from sqlalchemy import text
from schemes.api_router import router
from schemes.model import CreateUser

@router.post("/users", tags=["Users"], summary="Create user", status_code=201)
def create_user(post_user: CreateUser):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                INSERT INTO users (first_name, last_name, age)
                VALUES (:first_name, :last_name, :age)
                RETURNING *
            """),
            {
                "first_name": post_user.first_name,
                "last_name": post_user.last_name,
                "age": post_user.age,
            }
        )
        user = result.fetchone()
        
        return dict(user._mapping)