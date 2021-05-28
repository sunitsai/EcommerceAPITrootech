from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    is_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title


class Product(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.Name, self.price)

class Cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['cart_id', '-created_at']
        

    def __str__(self):
        return f'{self.cart_id}'
    