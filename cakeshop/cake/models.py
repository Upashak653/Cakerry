from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    Username=models.CharField(max_length=40)      
    Email = models.EmailField(null=True)
    Password = models.CharField(max_length=20)
    
class ItemList(models.Model):
    Category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Item_name = models.CharField(max_length=40)
    Description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList,related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    User_name=models.CharField(max_length=500)
    Description = models.TextField(blank=False)
    Rating=models.IntegerField(null=True)

    def __str__(self):
        return self.User_name


class Book_cake(models.Model):
    Name = models .CharField(max_length=20)
    Email_number = models.EmailField(null=True)
    Cake = models.CharField(null=True,max_length=20)
    Total_person = models.IntegerField(null=True)
    Occassion = models.CharField(max_length=20,null=True)
    Cake_size = models.CharField(max_length=20,null=True)
    Booking_date = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.Booking_date.strftime('%Y-%m-%d %H:%M:%S')

