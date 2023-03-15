from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
class SubCategory(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
     # slug = models.CharField(max_length=400, unique= True)
    def __str__(self):
        return self.name


STOCK = (('In stock','In stock'), ('Out of stock', 'Out of Stock'))
LABELS = (('new','new'),('sale','sale'),('','default'),('featured','featured'))
# SIZE = (('xs','xs'),('s','s'),('m','m'),('l','l'),('xl','xl'))

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to='image/')
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank= True )
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank= True )
   #brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null = True)
    stock = models.CharField( choices= STOCK,blank = True, max_length=30)
    labels = models.CharField(choices= LABELS, blank = True, max_length=30)
    # size = models.CharField(choices=SIZE, blank=True, max_length=30)

    def __str__(self):
        return self.name

# class FeaturedProduct(models.Model):
#     name = models.ForeignKey(Product.name)
#     image = models.ForeignKey(Product.image)
#     price = models.ForeignKey(Product.price)
#
#     products = models.ForeignKey(Product, on_delete=models.CASCADE, null= True, blank = True)
#
#     def __str__(self):
#         return self.name

class Order(models.Model):
    #customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)


    def __str__(self):
        return str(self.id)

class Carousel(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'media', null= "True")
    title1 = models.CharField(max_length=300 , null="True")
    title2 = models.CharField(max_length=300, null="True")
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media', null="True")
    description = models.CharField(max_length=300, null="True")

    def __str__(self):
        return self.name
