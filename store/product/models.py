from turtle import mode
from unicodedata import category
from django.db import models



class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField('Category Name', max_length=50)
    
    def __str__(self):
        """Unicode representation of Category."""
        return f'{self.name}'

class Sub_Category(models.Model):
    """Model definition for Sub_Category."""

    name = models.CharField('Sub Category Name', max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategorys', null=True)

    def __str__(self):
        """Unicode representation of Sub_Category."""
        return f'{self.name}'

class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField('product name', max_length=50)
    sku=models.CharField('Sku Key', max_length=50, blank=True, unique=True)
    descrption = models.TextField(default='')
    category = models.ManyToManyField('category', null=True)
    sub_category = models.ManyToManyField('Sub_Category',related_name='categorys')
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    false_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        """Unicode representation of Product."""
        return f'{self.name}'