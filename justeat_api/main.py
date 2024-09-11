from fastapi import FastAPI, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.security import APIKeyHeader
from typing import Dict, List, Optional
import os
from dotenv import load_dotenv
import models, schemas, database
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file
load_dotenv()

# Access the secret API key from the environment
SECRET_API_KEY = os.getenv("SECRET_API_KEY")

# Define API key dependency
api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

async def get_api_key(api_key: Optional[str] = Depends(api_key_header)) -> str:
    if api_key != SECRET_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return api_key

app = FastAPI()

origins=[
    "http://localhost:8000",
    "http://localhost:63343",
    "http://127.0.0.1:8000"
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)
@app.get("/justeat-data-r-and-d/", response_model=Dict[str, Dict[str, str]])
async def read_shops(
    api_key: str = Depends(get_api_key),
    db: AsyncSession = Depends(database.get_db),
    fields: Optional[List[str]] = Query(None, description="Select specific fields to include in the response")
):
    # Execute query to get all shops
    result = await db.execute(select(models.Shop))
    shops = result.scalars().all()  # Retrieve the ORM objects from the result set

    # Format the result based on selected fields
    if fields:
        formatted_result = {
            f"object_{shop.id}": {field: getattr(shop, field) for field in fields if hasattr(shop, field)}
            for shop in shops
        }
    else:
        # Return all fields if none are specified
        formatted_result = {
            f"object_{shop.id}": schemas.Shop.from_orm(shop).dict()
            for shop in shops
        }

    return formatted_result


@app.get("/foodhub-data-r-and-d/", response_model=Dict[str, Dict[str, str]])
async def read_foodhub(
    api_key: str = Depends(get_api_key),
    db: AsyncSession = Depends(database.get_db),
    fields: Optional[List[str]] = Query(None, description="Select specific fields to include in the response")
):
    # Execute query to get all records from FoodHub table
    result = await db.execute(select(models.FoodHub))
    foodhubs = result.scalars().all()  # Retrieve the ORM objects from the result set
    
    # Format the result based on selected fields
    if fields:
        fields_set = set(fields)
        formatted_result = {
            f"object_{foodhub.id}": {field: getattr(foodhub, field) for field in fields_set if hasattr(foodhub, field)}
            for foodhub in foodhubs
        }
    else:
        # Return all fields if none are specified
        formatted_result = {
            f"object_{foodhub.id}": schemas.FoodHub.from_orm(foodhub).dict()
            for foodhub in foodhubs
        }
    
    return formatted_result

