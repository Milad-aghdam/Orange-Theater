from sqlalchemy import Column, Integer, String
from database import Base

class Shop(Base):
    __tablename__ = "Justeat_p"

    id = Column(Integer, primary_key=True, index=True)
    Shop_id = Column(String(16), index=True)
    Name = Column(String(32))
    uniqueName = Column(String(32))
    City = Column(String(16))
    Area = Column(String(32))
    Address = Column(String(64))
    Postcode = Column(String(16))
    Lng = Column(String(32))
    Lat = Column(String(32))
    Rating = Column(String(16))
    starRating = Column(String(16))
    isNew = Column(String(16))
    openingTimeLocal = Column(String(64))
    Cuisines = Column(String(256))
    deliveryFees = Column(String(256))
    



class FoodHub(Base):
    __tablename__ = "Foodhub_l1"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(32))
    Description = Column(String(256), nullable=True)
    Phone = Column(String(16), nullable=True)
    Host = Column(String(32), nullable=True)
    URL = Column(String(256), nullable=True)
    Country = Column(String(32), nullable=True)
    Region = Column(String(32), nullable=True)
    City = Column(String(32), nullable=True)
    Street = Column(String(64), nullable=True)
    Number = Column(String(16), nullable=True)
    Postcode = Column(String(16), nullable=True)
    Latitude = Column(String(64), nullable=True)  # Latitude
    Longitude = Column(String(64), nullable=True)  # Longitude
    Rating = Column(String(16), nullable=True)
    Total_Reviews = Column(String(16), nullable=True)
    Opening_hours = Column(String(256), nullable=True)
    Review_Categories = Column(String(256), nullable=True)
    Cuisines = Column(String(256), nullable=True)
    Merchant_ID = Column(String(32), nullable=True)
    Delivery_Time = Column(String(32), nullable=True)
    Collection_Time = Column(String(32), nullable=True)
    Town = Column(String(32), nullable=True)
    Facebook = Column(String(64), nullable=True)
    Twitter = Column(String(64), nullable=True)
    Android_Link = Column(String(256), nullable=True)
    Title = Column(String(64), nullable=True)
    Keywords = Column(String(256), nullable=True)
    SEO = Column(String(256), nullable=True)


    
    

