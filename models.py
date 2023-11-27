from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship

from database import Base

metadata = MetaData()


class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    categories = Column(String, index=True)
    medicine = relationship("Medicine", back_populates="categories")

class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    categories_id = Column(Integer, ForeignKey("categories.id"))
    categories = relationship("Categories", backref="medicines")

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    header = Column(String, index=True)
    text = Column(String)



