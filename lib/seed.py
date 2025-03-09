# lib/seed.py

from faker import Faker
import random
from sqlalchemy.orm import sessionmaker
from models import engine, Game

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# Print a message so we know the seed file is running
print("Seeding games...")

# Clear out old data from the games table to avoid duplicates
session.query(Game).delete()
session.commit()

# Generate 50 random game records using a list comprehension.
# This syntax (the square brackets with 'for i in range(50)' at the end) is called a list comprehension.
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for i in range(50)
]

# Add the new game records to the session and commit to the database.
session.add_all(games)
session.commit()

print("Seed complete!")
