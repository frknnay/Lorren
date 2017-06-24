from django.conf.urls import url
from authors import views

urlpatterns = [
    url(r'^show/(\d+)/$', views.show_author, name='show_author'),
]
