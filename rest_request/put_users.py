from schemes.BD.database import engine
from schemes.api_router import router
from schemes.model import UpdateUser

from fastapi import HTTPException
from sqlalchemy import text

@router.put("/users/{user_id}", tags=["Users"], summary="Update user")
def update_user(user_id: int, put_user: UpdateUser):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                UPDATE users
                SET first_name = :first_name,
                    last_name = :last_name,
                    age = :age
                WHERE id = :user_id
                RETURNING *
            """),
            {
                "first_name": put_user.first_name,
                "last_name": put_user.last_name,
                "age": put_user.age,
                "user_id": user_id
            }
        )
        user = result.fetchone()
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found!"
            )
        
        return dict(user._mapping)