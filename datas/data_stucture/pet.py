from pydantic import BaseModel, Field


class PetCateory(BaseModel):
    ctg_id: int = Field(alias="id")
    ctg_name: int = Field(alias="name")


class PetTag(BaseModel):
    tag_id: int = Field(alias="id")
    tag_name: str = Field(alias="name")


class Pet(BaseModel):
    pet_id: int = Field(alias="id")
    ctg_dict: PetCateory
    pet_name: None | str
    tags: PetTag
    status: None | str
