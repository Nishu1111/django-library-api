from django.core.management.base import BaseCommand
from faker import Faker
from library.models import Book, Review
import random

class Command(BaseCommand):
    help = "Seed database with dummy books and reviews"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Custom author list
        author_list = ["J.K. Rowling", "George Orwell", "Agatha Christie", "Mark Twain", "J.K. Rowling", "George Orwell", "Agatha Christie", "Mark Twain", "Jane Austen", "Ernest Hemingway", "F. Scott Fitzgerald", "Leo Tolstoy","Charles Dickens","Gabriel García Márquez","Haruki Murakami","Stephen King","Paulo Coelho","C.S. Lewis","J.R.R. Tolkien","Dan Brown","Virginia Woolf","Franz Kafka","Arthur Conan Doyle","Khaled Hosseini","Salman Rushdie","Kazuo Ishiguro", "Maya Angelou", "Chinua Achebe", "Alice Walker", "Toni Morrison", "Roald Dahl", "William Shakespeare"]

        book_titles = [
    "To Kill a Mockingbird",
    "Pride and Prejudice",
    "The Great Gatsby",
    "War and Peace",
    "1984",
    "Animal Farm",
    "The Catcher in the Rye",
    "One Hundred Years of Solitude",
    "The Lord of the Rings",
    "Harry Potter and the Philosopher’s Stone",
    "Harry Potter and the Chamber of Secrets",
    "Harry Potter and the Prisoner of Azkaban",
    "Harry Potter and the Goblet of Fire",
    "Harry Potter and the Order of the Phoenix",
    "Harry Potter and the Half-Blood Prince",
    "Harry Potter and the Deathly Hallows",
    "The Hobbit",
    "The Chronicles of Narnia",
    "A Tale of Two Cities",
    "Les Misérables",
    "Crime and Punishment",
    "The Brothers Karamazov",
    "The Picture of Dorian Gray",
    "The Old Man and the Sea",
    "The Alchemist",
    "The Handmaid’s Tale",
    "The Kite Runner",
    "A Thousand Splendid Suns",
    "Midnight’s Children",
    "The God of Small Things",
    "Beloved",
    "Things Fall Apart",
    "I Know Why the Caged Bird Sings",
    "Wuthering Heights",
    "Great Expectations",
    "Dracula",
    "Frankenstein",
    "Moby-Dick",
    "The Adventures of Huckleberry Finn",
    "The Adventures of Tom Sawyer",
    "A Game of Thrones",
    "A Clash of Kings",
    "A Storm of Swords",
    "A Feast for Crows",
    "A Dance with Dragons",
    "The Da Vinci Code",
    "Angels and Demons",
    "Inferno",
    "Origin",
    "Brave New World"
    ]


        for _ in range(20):
            book = Book.objects.create(
                title=random.choice(book_titles),
                #to generate any name for book
                #title=fake.sentence(nb_words=3),
                # random choice from custom list
                author=random.choice(author_list),
                #generate fake full name
                # author=f"{fake.first_name()} {fake.last_name()}",
                published_date=fake.date_this_century(),
                genre=random.choice(["Fiction", "Non-Fiction", "Sci-Fi", "Fantasy", "kids-fun", "Manga"]),
            )

            for _ in range(3):
                Review.objects.create(
                    book=book,
                    reviewer_name=f"{fake.first_name()} {fake.last_name()}",
                    rating=random.randint(1, 5),
                    comment=fake.sentence(),
                )
            
        self.stdout.write(self.style.SUCCESS("Dummy data created!"))
