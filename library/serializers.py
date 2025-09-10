from rest_framework import serializers
from .models import Book, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Nested representation of reviews
    def get_reviews(self, obj):
        reviews = obj.reviews.all().order_by('id')  # sort by review ID
        return ReviewSerializer(reviews, many=True).data
    

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "published_date",
            "genre",
            "reviews",   
        ]
