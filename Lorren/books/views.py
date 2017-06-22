from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book

def home_page(request):
    books = Book.objects.all()
    return render(request, 'books/home.html',{'books': books})

def book_details(request, book_id):
    return render(request, 'books/book_detail.html')
