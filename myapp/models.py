from django.db import models

# Create your models here.
class register(models.Model):
    Full_name=models.CharField(max_length=28)
    Username=models.CharField(max_length=28,unique=True)
    Email=models.CharField(max_length=28,)
    Phone_Number=models.IntegerField()
    Password=models.CharField(max_length=20)

class booking(models.Model):
    userid = models.IntegerField()
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    petname=models.CharField(max_length=100)
    petspecies=models.CharField(max_length=100)
    bkdate=models.DateField()
    bktime= models.CharField(max_length=15)
    service=models.CharField(max_length=100)
    charge= models.IntegerField()
    status=models.CharField(max_length=100, default="New Booking")

class feedback(models.Model):
    uname = models.CharField(max_length=50,unique=True)
    ph= models.CharField(max_length=50,unique=True)
    feed = models.CharField(max_length=550)
