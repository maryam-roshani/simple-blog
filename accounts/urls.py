from . import views
from django.urls import path, re_path as url
from django.urls import include, re_path


app_name= 'accounts'

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout'),
]

