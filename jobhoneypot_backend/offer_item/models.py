from django.db import models
import json
from django.forms.models import model_to_dict
# Create your models here.
class Offer(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200,default="Default Title")
    link = models.CharField(max_length=200,default="randomurl")
    category = models.CharField(max_length=200,default="my-category")
    contractType = models.CharField(max_length=200,default="full-time")
    salaryMax = models.CharField(max_length=200,default="0€")

    class Meta:
        ordering = ('id',)




class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    key_name = models.CharField(max_length=200,default=None)
    val_name = models.CharField(max_length=200,default=None)
class Skill(models.Model):
    ski_id = models.IntegerField(primary_key=True)
