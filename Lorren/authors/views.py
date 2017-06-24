from django.shortcuts import render, redirect

from authors.models import Author


def show_author(request, author_id):
    author = Author.objects.get(id=author_id)
    author_books = author.book_set.all()
    return render(request, 'authors/author_detail.html',
        {'author': author, 'author_books': author_books})

def new_author(request):
    if request.method == 'POST':
        Author.objects.create(name=request.POST['name'])
        return redirect('home')
    else:
        return render(request, 'authors/add_author.html')

def list_authors(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})
