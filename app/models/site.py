#Importing Libraries
from pydantic import BaseModel
from typing import Optional


# defining the Site model for the database
class Site(BaseModel):

    id: Optional[str] = None
    
    site_name: str
    address: str
    latitude: float
    longitude: float