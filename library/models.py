from django.db import models

# Create your models here.
#books
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} by {self.author}"

#reviewer
class Review(models.Model):
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE) #one to many 
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.reviewer_name} rated {self.book.title} {self.rating}/5"

