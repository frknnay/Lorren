from django.conf.urls import url
from authors import views

urlpatterns = [
    url(r'^show/(\d+)/$', views.view_author, name='view_author'),
]
