#type: ignore
import os
import sys
import requests
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from shared.database import Rawpost, SessionLocal

class HackerNewsScraper():
    """"""
    BASE_URL = "https://hacker-news.firebaseio.com/v0"

    def __init__(self):
        self.session = requests.Session()
    
    def get_top_stories(self, limit: int = 50) -> list[int]:
        """"""
        url = f"{self.BASE_URL}/topstories.json"
        response = self.session.get(url)
        response.raise_for_status()
        story_ids = response.json()
        return story_ids[:limit]
    
    def get_story_details(self, story_id: int) -> dict:
        """"""
        url = f"{self.BASE_URL}/item/{story_id}.json"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    
    def save_to_database(self, db: Session, story: dict) -> bool:
        """"""
        existing = db.query(Rawpost).filter(
            Rawpost.source == "hackernews",
            Rawpost.source_id == str(story['id'])
        ).first()

        if existing:
            print(f"Story {story['id']} already exists. Skipping...")
            return False
        return None

