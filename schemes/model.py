from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=64)
    age: int = Field(ge=0, le=150)