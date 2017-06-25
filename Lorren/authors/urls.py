from django.conf.urls import url
from authors import views

app_name = 'authors'

urlpatterns = [
    url(r'^$', views.list_authors, name='list_authors'),
    url(r'^new$', views.new_author, name='new_author'),
    url(r'^show/(\d+)/$', views.show_author, name='show_author'),
    url(r'^show/(\d+)/edit$', views.edit_author, name='edit_author'),
    url(r'^show/(\d+)/delete$', views.delete_author, name='delete_author'),
]
