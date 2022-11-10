from django.contrib import admin
from django.urls import path, re_path as url, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from myApp import views as book_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', book_views.book_list),
    url(r'^about/$', views.about),
    url(r'^books/', include('myApp.urls')),
    url(r'^accounts/', include('accounts.urls')),
]


#urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)