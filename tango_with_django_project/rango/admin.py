from django.contrib import admin
from rango.models import Category, Page
from django import views
# class CategoryAdmin(admin.ModelAdmin):
# prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','views','likes')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
