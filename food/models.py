from django.db import models

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)  # This will be used for categories
    category_image = models.CharField(max_length=255)  # Static image name for categories
    image = models.ImageField(upload_to='products/')  # Path for product images
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    stock_quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
