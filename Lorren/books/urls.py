from django.conf.urls import url
from books import views


app_name = 'books'

urlpatterns = [
    url(r'^show/(\d+)/$', views.show_book, name="show_book"),
]
