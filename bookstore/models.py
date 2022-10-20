from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,null=True ,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    CATEGORY = (
        ('Fiction', 'Fiction'),
        ('Biography', 'Biography'),
        ('History', 'History'),
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Mathematics', 'Mathematics'),
    )
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    tags = models.ManyToManyField(Tag)
    category = models.CharField(max_length=100, choices=CATEGORY)
    description = models.CharField(max_length=1000, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
        ('Processing', 'Processing'),
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.book.name