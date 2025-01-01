from django.db import models

# Create your models here.

class StudentORM(models.Model):
    name = models.CharField(max_length=80)
    phoneNo = models.IntegerField()
    stClass = models.IntegerField()
    score = models.IntegerField()
    profile= models.ImageField(upload_to="pics")
