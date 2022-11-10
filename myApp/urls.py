from . import views
from django.urls import path, re_path as url
from django.urls import include, re_path


app_name= 'myApp'

urlpatterns = [
    url(r'^$', views.book_list, name='list'),
    url(r'^create/$', views.book_create, name='create'),
    re_path(r'^(?P<slug>[-\w]+)/$', views.book_detail, name='detail'),
    
]

