
from django.conf.urls import url, include

from books import views as books_views
from books import urls as books_urls

from authors import urls as authors_urls

urlpatterns = [
    url(r'^$', books_views.home_page, name='home'),
    url(r'^books/', include(books_urls)),
    url(r'^authors/', include(authors_urls)),

]
