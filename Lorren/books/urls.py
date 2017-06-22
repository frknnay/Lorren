from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^(\d+)/$', views.book_details, name="book_details"),
]
