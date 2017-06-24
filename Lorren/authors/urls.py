from django.conf.urls import url
from authors import views

urlpatterns = [
    url(r'^$', views.list_authors, name='list_authors'),
    url(r'^show/(\d+)/$', views.show_author, name='show_author'),
    url(r'^new$', views.new_author, name='new_author')
]
