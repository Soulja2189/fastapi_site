from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from database import SessionLocal, db
from schema import MedicineCreate, CategoriesCreate, News
from models import Categories, Medicine

app = FastAPI()


medicines = []
news = []
categories = []


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/medicines/")
async def create_medicine(medicine: MedicineCreate):
    db = SessionLocal()
    new_medicine = Medicine(name=medicine.name, description=medicine.description, categories_id=medicine.categories_id)
    db.add(new_medicine)
    db.commit()
    db.refresh(new_medicine)
    return {"message": "Лекарство успешно создано", "medicine": new_medicine}


@app.get("/medicines/")
async def get_medicines():
    medicines = db.query(Medicine).all()
    return {"medicines": medicines}


@app.get("/medicines/{medicine_id}")
async def get_medicine(medicine_id: int):
    if medicine_id < len(medicines):
        return {"medicine": medicines[medicine_id]}
    else:
        return {"error": "Лекарство не найдено"}

# Удаление лекарства
# @app.delete("/medicines/{medicine_id}")
# async def delete_medicine(medicine_id: int):
#     if medicine_id < len(medicines):
#         medicines.pop(medicine_id)
#         return {"message": "Лекарство успешно удалено"}
#     else:
#         return {"error": "Лекарство не найдено"}
#
# # Обновление информации о лекарстве
# @app.put("/medicines/{medicine_id}")
# async def update_medicine(medicine_id: int, medicine: Medicine):
#     if medicine_id < len(medicines):
#         medicines[medicine_id] = medicine
#         return {"message": "Информация о лекарстве успешно обновлена"}
#     else:
#         return {"error": "Лекарство не найдено"}
#


@app.post("/categories/")
async def create_category(category: CategoriesCreate):
    db = SessionLocal()
    new_category = Categories(categories=category.categories)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return {"message": "Категория успешно создана", "category": new_category}


@app.get("/categories/")
async def get_categories():
    categories = db.query(Categories).all()
    return {"categories": categories}


@app.get("/medicine{category_id}")
async def get_medications_by_category(categories_id: int):
    meds_in_categories = [med for med in medicines if med.categories_id == categories_id]
    return {"medications": meds_in_categories}



@app.post("/news/")
async def create_news(news_item: News):
    news.append(news_item)
    return {"message": "Новость успешно создана"}


@app.get("/news/")
async def get_news():
    return {"news": news}


@app.get("/news/{news_id}")
async def get_news_item(news_id: int):
    if news_id < len(news):
        return {"news_item": news[news_id]}
    else:
        return {"error": "Новость не найдена"}

# Удаление новости
# @app.delete("/news/{news_id}")
# async def delete_news(news_id: int):
#     if news_id < len(news):
#         news.pop(news_id)
#         return {"message": "Новость успешно удалена"}
#     else:
#         return {"error": "Новость не найдена"}
#
# # Обновление информации о новости
# @app.put("/news/{news_id}")
# async def update_news(news_id: int, news_item: News):
#     if news_id < len(news):
#         news[news_id] = news_item
#         return {"message": "Информация о новости успешно обновлена"}
#     else:
#         return {",,error": "Новость не найдена"}