from django.db import models
from datetime import datetime
from apps.category.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=True) 
    compare_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    quantity = models.IntegerField(default=20, blank=True)
    sold = models.IntegerField(default=0, blank=True)
    date_created = models.DateTimeField(default=datetime.now)

    def get_thumbnail(self):
        if self.photo:
            return self.photo.url
        return ''

    def __str__(self):
        return self.name