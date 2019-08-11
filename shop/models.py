from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import Permission, User
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True )
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    thumbnail = models.ImageField(upload_to='products/thumbnails', blank=True)
    author = models.CharField(max_length=50,db_index=True,default='Author_Name')
    publisher = models.CharField(max_length=50,db_index=True,default='Publisher_Name')
    isbn_no = models.CharField(max_length=50,db_index=True,default='isbn_no')

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

class Myrating(models.Model):
    user    = models.ForeignKey(User,related_name='rating',on_delete=models.CASCADE) 
    product = models.ForeignKey(Product,related_name='rated_products',on_delete=models.CASCADE)
    rating  = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])
    
    def __str__(self):
        return 'Rated Book: {}'.format(self.product)

    def get_absolute_url(self):
         return reverse('shop:product_detail', args=[self.id, self.slug])
