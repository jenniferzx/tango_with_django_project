from django.urls import URLPattern, path
from rango import views

app_name ='rango'

urlpatterns = [
    path(r'rango/', views.index , name='index'),
    path(r'rango/about/', views.about , name='about'),
]