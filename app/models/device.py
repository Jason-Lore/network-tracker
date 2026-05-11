#Importing Libraries
from pydantic import BaseModel
from typing import Optional
from bson import ObjectId


# defining the Device model for the database
class Device(BaseModel):

    id: Optional[str] = None

    device_name: str
    device_type: str

    site_id: str

    rack_location: Optional[str] = None
    unit_location: Optional[str] = None
    floor: Optional[str] = None
    closet: Optional[str] = None
    cabinet: Optional[str] = None

    ip_address: Optional[str] = None

    is_online: Optional[bool] = None
    last_checked: Optional[str] = None
    ping_success_count: Optional[int] = 0