from django.urls import URLPattern, path
from rango import views

app_name ='rango'

urlpatterns = [
    path(r'rango/', views.index , name='index'),
    path(r'rango/about/', views.about , name='about'),
    path(r'rango/category/<slug:category_name_slug>/',views.show_category, name='show_category'),
]