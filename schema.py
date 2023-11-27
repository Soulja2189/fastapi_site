from pydantic import BaseModel

class MedicineCreate(BaseModel):
    name: str
    description: str
    categories_id: int

class News(BaseModel):
    header: str
    text: str

class CategoriesCreate(BaseModel):
    categories: str