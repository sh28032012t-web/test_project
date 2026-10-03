from schemes.BD.database import engine
from sqlalchemy import text
from fastapi import HTTPException
from schemes.api_router import router
from schemes.model import ResponseUser

@router.get("/users/{user_id}", tags=["Users"], summary="Find user")
def find_user(user_id: int):
    with engine.connect() as connection:
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
        user = result.fetchone()
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found!"
            )
        
        return ResponseUser(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            age=user.age,
        )