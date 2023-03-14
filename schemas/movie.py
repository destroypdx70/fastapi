from pydantic import BaseModel, Field
from typing import Optional, List

class movie(BaseModel):
    id: Optional[int] = None 
    title: str = Field(min_length=5,max_length=50)
    overview: str = Field(min_length=15,max_length=50)
    year: int = Field(le=2005)
    rating: float = Field(ge=1,le=10)
    category: str = Field(min_length=5,max_length=15)

    class Config:
        schema_extra = {
            "example" : {
                "id" : 1,
                "title" : "A movie with my love",
                "overview" : "Descrption of the movie with my love Anyi",
                "year" : 2005,
                "rating" : 1.000000000000000000000,
                "category" : "Action"
            }
        }