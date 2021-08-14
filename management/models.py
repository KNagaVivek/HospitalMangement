from django.db import models
from django.utils.regex_helper import Choice
from django.utils.timezone import  now
# Create your models here.


class cart_item(models.Model):
    Img = models.ImageField(upload_to='pics')
    Product = models.CharField(max_length=255)
    Quantity = models.IntegerField()
    Price = models.FloatField()
    Total = models.FloatField()
    def __str__(self):
        return self.Product

class Modify(models.Model):
    title = models.CharField(max_length=50)
    # des = models.CharField(max_length=500)
    Lab_img = models.ImageField(upload_to='pics')
    Pharmacy_img = models.ImageField(upload_to='pics')
    equipments_img1 = models.ImageField(upload_to='pics')
    equipments_img2 = models.ImageField(upload_to='pics')
    number = models.BigIntegerField()
    add = models.CharField(max_length=200)

class appointment(models.Model):
    name = models.CharField(max_length=50)
    Phone_Number = models.BigIntegerField()
    problem = models.TextField()
    appointment_Date = models.DateTimeField(auto_now_add=True,auto_now=False,blank=True,null=True)
    Sent_Time = models.DateTimeField(default=now,blank=True)
    # def __str__(self):
    #     return self.name

class pharmacy_order(models.Model):
    DISTRICT_CHOICE = (
        (1,'Anantapur'),
        (2,'Chittoor'),
        (3,'East Godavari'), 
        (4,'Guntur'),
        (5,'YSR Kadapa'),
        (6,'Krishna'),
        (7,'Kurnool'),
        (8,'Nellore'),
        (9,'Prakasam'),
        (10,'Srikakulam'),
        (11,'Vijayanagaram'),
        (12,'Visakapatnam'),
        (13,'West Godavari'),
    )
    District = models.CharField(max_length=50,choices=DISTRICT_CHOICE)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=500)
    pincode = models.IntegerField()
    Phone_Number = models.PositiveBigIntegerField()
    order = models.TextField()
    def __str__(self):
        return self.First_Name