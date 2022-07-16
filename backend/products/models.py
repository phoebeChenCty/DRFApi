from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)


'''
in Django shell:
>>> from products.models import Product
>>> Product.objects.create(title='Hello world', content='this is amazing!', price=0.00)
<Product: Product object (1)>
>>> Product.objects.create(title='Hello world again', content='this is amazing!', price=12.00)
<Product: Product object (2)>
>>> Product.objects.all().order_by("?").first() # get random Product
<Product: Product object (1)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (1)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (1)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (2)>
'''
