from django.db import models
from django.db.models.fields.related import ForeignKey

from FoodDistribution.authentification_app.models import DistributionSite

class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name    



class Product(models.Model):
    name = models.CharField(max_length=255)
    category = ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True) # Modifié ici
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']  

    def __str__(self):
        return self.name     

class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity}"

class Order(models.Model):
    date_order = models.DateTimeField(auto_now_add=True)
    distribution_site = models.ForeignKey(DistributionSite, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')

    class Meta:
        ordering = ['-date_order']

    def __str__(self):
        return self.distribution_site.name  

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
