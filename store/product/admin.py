from django.contrib import admin
from .models import Category,Sub_Category,Product

# Register your models here.


class Sub_CategoryInline(admin.TabularInline):
    '''Tabular Inline View for Brand'''

    model = Sub_Category
    verbose_name = 'Sub_Category'
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('name',)
    inlines = [Sub_CategoryInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('name',)
    filter_horizontal = ('category','sub_category')