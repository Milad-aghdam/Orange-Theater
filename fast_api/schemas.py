from pydantic import BaseModel ,validator
from typing import Optional  # Import Optional

class ShopBase(BaseModel):
    Shop_id: str
    Name: str
    uniqueName: str
    City: str
    Area: str
    Address: str
    Postcode: str
    Rating: str
    starRating: str
    isNew: str
    openingTimeLocal: str
    Cuisines: str
    deliveryFees: str

class Shop(ShopBase):
    id: int

    class Config:
        orm_mode = True  # Ensure orm_mode is set to True
        from_attributes=True




class FoodHubBase(BaseModel):
    Name: str
    Description: Optional[str] = None
    Phone: Optional[str] = None
    Host: Optional[str] = None
    URL: Optional[str] = None
    Country: Optional[str] = None
    Region: Optional[str] = None
    City: Optional[str] = None
    Street: Optional[str] = None
    Number: Optional[str] = None
    Postcode: Optional[str] = None
    Latitude: Optional[str] = None  # Latitude
    Longitude: Optional[str] = None  # Longitude
    Rating: Optional[str] = None
    Total_Reviews: Optional[str] = None
    Opening_hours: Optional[str] = None
    Review_Categories: Optional[str] = None
    Cuisines: Optional[str] = None
    Merchant_ID: Optional[str] = None
    Delivery_Time: Optional[str] = None
    Collection_Time: Optional[str] = None
    Town: Optional[str] = None
    Facebook: Optional[str] = None
    Twitter: Optional[str] = None
    Android_Link: Optional[str] = None
    Title: Optional[str] = None
    Keywords: Optional[str] = None
    SEO: Optional[str] = None

    # Validator to handle null or empty strings and convert them to None
    @validator('*', pre=True, always=True)
    def convert_empty_to_none(cls, v):
        if v is None or v == "":
            return None  # or return a default value if needed
        return v

class FoodHub(FoodHubBase):
    id: int

    class Config:
        orm_mode: True
    