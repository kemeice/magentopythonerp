from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models

# Create your models here.
class Catalog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=False, auto_now=True)


class CatalogCategory(models.Model):
    catalog = models.ForeignKey('Catalog',
                                related_name='categories')
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)


class Product(models.Model):
    category = models.ForeignKey('CatalogCategory',
                                 related_name='products')
    PRODUCT_CHOICES = (
        ('simple', 'Simple'),
        ('configurable', 'Configurable'),
        ('grouped', 'Grouped'),
        ('bundle', 'Bundle'),
    )

    DEV_CHOICES = (
        ('3day', 'Three Days'),
        ('7days', 'Seven Days'),
        ('14days', 'Fourteen Days'),
        ('21 Days', 'Twenty One Days'),
    )

    GROUP_CHOICES = (
        ('Default', 'Default'),
        ('Beds', 'Beds'),

    )
    type_product = models.CharField('Product type', max_length=50,
                                    choices=PRODUCT_CHOICES, default='simple')
    delivery = models.CharField('Delivery time', max_length=50,
                                    choices=DEV_CHOICES, default='Please select')
    groups = models.CharField('Websites', max_length=50,
                                    choices=GROUP_CHOICES , default='Please select')

    weight= models.CharField(max_length=10, default=5)
    stock = models.CharField(max_length=10,null=True, blank=True)
    supplier= models.CharField(max_length=120,null=True, blank=True)
    supplier_sku = models.CharField(max_length=120,null=True, blank=True)
    order_per_X = models.CharField(max_length=10,null=True, blank=True )
    supplier_delivery_time= models.CharField(max_length=10,default=7 )
    membis_be_Nederlands= models.BooleanField(default=False)
    membis_be_France= models.BooleanField(default=False)
    membis_nl_Nederlads= models.BooleanField(default=False)
    Horeca= models.BooleanField(default=False)
    Color= models.CharField(max_length=120,null=True, blank=True )
    height=models.CharField(max_length=120,null=True, blank=True )
    width=models.CharField(max_length=120,null=True, blank=True )
    lenght=models.CharField(max_length=120,null=True, blank=True )

    size=models.CharField(max_length=120,null=True, blank=True )
    advantage_1= models.CharField(max_length=120,null=True, blank=True )
    advantage_2= models.CharField(max_length=120,null=True, blank=True )
    advantage_3= models.CharField(max_length=120,null=True, blank=True)


    name = models.CharField(max_length=120)
    shortdescription = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100,
                                     null=True, blank=True)
    #slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title


    def get_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse("single_product", kwargs={"slug": self.slug})



class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/images/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.product.title


class ProductDetail(models.Model):
    product = models.ForeignKey('Product',
                                related_name='details')
    attribute = models.ForeignKey('ProductAttribute')
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s: %s - %s' % (self.product,
                                 self.attribute,
                                 self.value)


class ProductAttribute(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % self.name


class Mageconnect(models.Model):
    storeurl = models.TextField(blank=True)
    key = models.TextField(blank=True)
    user = models.TextField(blank=True)
