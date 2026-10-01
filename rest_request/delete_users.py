from schemes.api_router import router
from schemes.BD.database import engine
from sqlalchemy import text
from fastapi import HTTPException

@router.delete("/users/{user_id}", tags=["Users"], summary="Remove user", status_code=204)
def delete_user(user_id: int):
    with engine.begin() as connection:
        result = connection.execute(
            text("""
                DELETE FROM users
                WHERE id = :user_id
                RETURNING *
            """),
            {
                "user_id": user_id,
            }
        )
        user = result.fetchone()
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found!"
            )
        
        return None