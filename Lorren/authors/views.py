from django.shortcuts import render, redirect, reverse

from authors.models import Author


def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})

def show_author(request, author_id):
    author = Author.objects.get(id=author_id)
    author_books = author.book_set.all()
    return render(request, 'authors/author_detail.html',
        {'author': author, 'author_books': author_books})

def new_author(request):
    if request.method == 'POST':
        author = Author.objects.create(name=request.POST['name'])
        return redirect('authors:show_author', author.id)
    else:
        return render(request, 'authors/add_author.html')

def edit_author(request, author_id):
    author = Author.objects.get(id=author_id)

    if request.method == 'POST':
        author.name = request.POST['name']
        author.save()
        return redirect('authors:show_author', author_id)

    return render(request, 'authors/edit_author.html', {'author': author})
