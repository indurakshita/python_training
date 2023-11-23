from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Article(BaseModel):
    id: str = Field(alias="article_id")
    category: List[str]
    content: str
    country: List[str]
    creator: Optional[List[str]]
    description: str
    image_url: Optional[str]
    keywords: Optional[List[str]]
    language: Optional[str]
    link: str
    pub_date: datetime = Field(alias="pubDate")
    source_id: str
    source_priority: int
    title: str
    video_url: Optional[str]
    




