from django.db import models

# Create your models here.
class Offer(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,default=None)
    link = models.CharField(max_length=200,default=None)
    category = models.CharField(max_length=200,default=None)
    contractType = models.CharField(max_length=200,default=None)
    salaryMax = models.CharField(max_length=200,default=None)

class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    key_name = models.CharField(max_length=200,default=None)
    val_name = models.CharField(max_length=200,default=None)
