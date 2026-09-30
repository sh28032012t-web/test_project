from schemes.BD.database import engine
from sqlalchemy import text
from fastapi import APIRouter, HTTPException

router = APIRouter()

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
        
        return dict(user._mapping)