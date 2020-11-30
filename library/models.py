from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, timedelta



class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=600)
    ijod_yoli = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} | {self.ijod_yoli}'


class Book(models.Model):
    name = models.CharField(max_length=600)
    author = models.CharField(max_length=500, null=True)
    eddition = models.IntegerField()
    publication = models.IntegerField()
    category = models.CharField(max_length=500, null=True)
    cost = models.FloatField()
    amount = models.IntegerField()
    img = models.ImageField(upload_to='books', null=True)
    pages = models.IntegerField(null=True)
    description = models.TextField(null=True)
    language = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} '


class Reader(models.Model):
   # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='reader')
    phone = models.CharField(max_length=13, null=True)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Foydalanuvchilar'
        verbose_name_plural = "Foydalanuvchilar"


class Received(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    received_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    returned_at = models.DateField(default=datetime.now()+timedelta(days=10))


    def __str__(self):
        return f'{self.reader.full_name}  ||  {self.book.name}  ||  {self.received_at}'


class HLog(models.Model):
    user = models.ForeignKey(Reader, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}  | {self.book}'


@receiver(post_save, sender=Received)
def create_log_orders(sender, instance, **kwargs):
    mylog = HLog.objects.create(user=instance.reader, book=instance.book)
    return mylog






class Menu(models.Model):
    order = models.IntegerField(null=True)
    name = models.CharField(max_length=40, null=True)
    link = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class SideBar(models.Model):
    order = models.IntegerField(null=True)
    name = models.CharField(max_length=40, null=True)
    link = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def parts(self):
        return SubMenu.objects.filter(menu=self)

    def __str__(self):
        return self.name


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    order = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.menu.name}    ||     {self.name}'






# Create your models here.
