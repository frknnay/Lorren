from django.conf.urls import url
from books import views


app_name = 'books'

urlpatterns = [
    url(r'^$', views.home_page, name="list_books"),
    url(r'^new$', views.new_book, name="new_book"),
    url(r'^show/(\d+)/$', views.show_book, name="show_book"),
    url(r'^show/(\d+)/edit$', views.edit_book, name="edit_book"),
    url(r'^show/(\d+)/delete$', views.delete_book, name="delete_book"),
    url(r'^show/(\d+)/rate$', views.rate_book, name="rate_book"),


]
