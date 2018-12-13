from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.main, name='main'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^category/(\w+)', views.page_category, name='page_category'),
]
