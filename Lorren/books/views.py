from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.models import Book

def home_page(request):
    books = Book.objects.all()
    return render(request, 'books/home.html',{'books': books})

def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.year = request.POST['year']
        book.save()
        return redirect('books:show_book', book_id)

    return render(request, 'books/edit_book.html', {'book': book})

def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect('home_page')
