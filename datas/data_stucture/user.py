from pydantic import BaseModel, Field


class User(BaseModel):
    user_id: int = Field(alias="id")
    username: None | str
    firstName: None | str
    lastName:  None | str
    email:  None | str
    phone:  None | str
    userStatus: int
