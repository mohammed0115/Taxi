from django.contrib import admin
from Categories.models import Categories
# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
   
    fields = (
        'name','price'
    )
    list_display = ['name','price']
admin.site.register(Categories, CategoriesAdmin)