from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Location(BaseModel):
    name: str
    region: str
    country : str
    lat: float
    lon: float
    localtime: datetime

class Current(BaseModel):
    last_updated: Optional[datetime]
    temp_c: float
    temp_f: float
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    location: Location

