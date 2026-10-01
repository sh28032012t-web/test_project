from pydantic import BaseModel, Field

class CreateUser(BaseModel):
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=64)
    age: int = Field(ge=0, le=150)

class DeleteUser(BaseModel):
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=64)
    age: int = Field(ge=0, le=150)

class UpdateUser(BaseModel):
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=64)
    age: int = Field(ge=0, le=150)

class ResponseUser(BaseModel):
    id: int
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=64)
    age: int = Field(ge=0, le=150)