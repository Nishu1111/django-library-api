from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ["id", "title", "author"]  #search fields
    filterset_fields = ['id', 'author', 'published_date']  #filterable fields

    @action(detail=False, methods=['get'])
    def top_rated(self, request):
        #Returns books ordered by average rating (top-rated first)
        # Annotate books with average rating
        books = Book.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating', 'id') #[:5] top 5
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "rating", "book"]  # /reviews/?rating=5

