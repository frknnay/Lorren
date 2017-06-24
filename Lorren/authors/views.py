from django.shortcuts import render

from authors.models import Author


def view_author(request, author_id):
    author = Author.objects.get(id=author_id)
    author_books = author.book_set.all()
    return render(request, 'authors/author_detail.html',
        {'author': author, 'author_books': author_books})
