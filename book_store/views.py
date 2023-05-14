from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg

from .models import Book


# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    return render(request, 'book_store/index.html', {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating,
    })


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, 'book_store/book_detail.html', {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling,
    })