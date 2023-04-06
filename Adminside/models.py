from django.db import models


# Create your models here.
class admindb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Username = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)


class catdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Description = models.TextField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to="category_img", null=True, blank=True)


class prodb(models.Model):
    Category = models.CharField(max_length=50, null=True, blank=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    Price = models.CharField(max_length=50, null=True, blank=True)
    Quantity = models.IntegerField()
    Description = models.CharField(max_length=300, null=True, blank=True)
    Image = models.ImageField(upload_to="category_img", null=True, blank=True)

class contactdb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Subject=models.TextField(max_length=100,null=True,blank=True)
    Message=models.TextField(max_length=100,null=True,blank=True)
