from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.models import Book, Comment
from authors.models import Author

def home_page(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'books/home.html',{'books': books})

def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def new_book(request):
    if request.method == 'POST':
        author = Author.objects.get(id=request.POST['author'])
        book = Book.objects.create(
            title=request.POST['title'],
            author=author,
            year=request.POST['year'],)
        return redirect('books:show_book', book.id)
    authors = Author.objects.all()
    return render(request, 'books/add_book.html', {'authors': authors})

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    authors = Author.objects.all()
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = Author.objects.get(id=request.POST['author'])
        book.year = request.POST['year']
        book.save()
        return redirect('books:show_book', book_id)

    return render(request, 'books/edit_book.html', {'book': book, 'authors': authors})

def delete_book(request, book_id):
    Book.objects.get(id=book_id).delete()
    return redirect('home_page')

def rate_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        Comment.objects.create(book=book,rating=request.POST['rating'])

    return redirect('books:show_book', book_id)
