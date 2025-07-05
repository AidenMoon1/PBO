# Abstract class
from abc import ABC, abstractmethod

class Artwork(ABC):
    def __init__(self, title, date, mood):
        self.title = title
        self.date = date
        self.mood = mood

    @abstractmethod
    def display_info(self):
        pass

# Lukisan turunan dari Artwork
class Painting(Artwork):
    def __init__(self, title, date, mood, medium):
        super().__init__(title, date, mood)
        self.medium = medium

    def display_info(self):
        return f"Painting: {self.title} | Medium: {self.medium} | Date: {self.date} | Mood: {self.mood}"

# Puisi turunan dari Artwork
class Poem(Artwork):
    def __init__(self, title, date, mood, theme):
        super().__init__(title, date, mood)
        self.theme = theme

    def display_info(self):
        return f"Poem: {self.title} | Theme: {self.theme} | Date: {self.date} | Mood: {self.mood}"

# Manajer data (JSON)
import json
import os

class ArtManager:
    def __init__(self, filepath='data/artworks.json'):
        self.filepath = filepath
        self.artworks = []
        self.load_data()

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        self.save_data()

    def save_data(self):
        data = [vars(a) | {'type': a.__class__.__name__} for a in self.artworks]
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def load_data(self):
        if not os.path.exists(self.filepath):
            return
        with open(self.filepath, 'r') as f:
            data = json.load(f)
            for item in data:
                if item['type'] == 'Painting':
                    self.artworks.append(Painting(item['title'], item['date'], item['mood'], item['medium']))
                elif item['type'] == 'Poem':
                    self.artworks.append(Poem(item['title'], item['date'], item['mood'], item['theme']))
