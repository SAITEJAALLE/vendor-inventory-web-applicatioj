from django.db import models
from django.conf import settings

class Product(models.Model):
    vendor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'is_vendor': True}
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Product: {self.name} by {self.vendor.username}"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'is_user': True}
    )
    quantity = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - Product: {self.product.name}, User: {self.user.username}"
