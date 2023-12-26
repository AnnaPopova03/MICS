from datetime import datetime


class Book:
    def __init__(self, title, author, category, release_date):
        self.title = title
        self.author = author
        self.category = category
        self.release_date = datetime.strptime(release_date, '%Y-%m-%d')

    def __str__(self):
        return f"{self.title} by {self.author} ({self.category})"