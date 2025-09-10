# Django Library API
This is a Django REST Framework project for managing books and reviews.

## Features
- Book & Review models
- Nested reviews in book detail
- Filter books by author and published date
- Search books by title and author
- Top-rated books endpoint (`/api/books/top_rated/`)
- Seeder command for dummy data (Faker & random books)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/<username>/django-library-api.git
cd django-library-api
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run migrations:

bash
Copy code
python manage.py migrate
Seed dummy data (optional):

bash
Copy code
python manage.py seed_books
Run the server:

bash
Copy code
python manage.py runserver
API Endpoints:

/api/books/ - list/create books

/api/books/<id>/ - book detail with nested reviews

/api/books/top_rated/ - top-rated books

/api/reviews/ - list/create reviews

License
MIT

sql
Copy code

Then stage and commit:

```bash
git add README.md
git commit -m "Add README.md"
git push
