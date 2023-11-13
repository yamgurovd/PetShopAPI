from pydantic import BaseModel, Field
import datetime


class OrderStore(BaseModel):
    order_id: int = Field(alias="id")
    pet_id: int = Field(alias="PetId")
    quantity: None | str
    ship_date: datetime.datetime = Field(alias="shipDate")
    status: int
    complete: str
