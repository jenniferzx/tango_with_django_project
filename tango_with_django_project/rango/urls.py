from telnetlib import STATUS
from django.urls import URLPattern, path
from rango import views


app_name ='rango'

urlpatterns = [
    path(r'',views.index,name='index'),
    path(r'rango/', views.index , name='index'),
    path(r'rango/about/', views.about , name='about'),
    path(r'rango/category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    path(r'rango/add_category/', views.add_category, name='add_category'),
    path(r'rango/category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path(r'rango/register/', views.register, name='register'), # New mapping!
    path(r'rango/login/', views.user_login, name='login'),
    path(r'rango/restricted/', views.restricted, name='restricted'),
    path(r'rango/logout/', views.user_logout, name='logout'),
    




]