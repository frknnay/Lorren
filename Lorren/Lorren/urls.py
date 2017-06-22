
from django.conf.urls import url
from django.contrib import admin

from books import views as books_views


urlpatterns = [
    url(r'^$', books_views.home_page, name='home'),
]
