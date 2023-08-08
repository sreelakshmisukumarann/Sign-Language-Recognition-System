from django.db import models

# Create your models here.
class registermodel(models.Model):
    name1=models.CharField(max_length=200,null=True)
    addr=models.CharField(max_length=200,null=True)
    dob=models.CharField(max_length=200,null=True)
    age=models.CharField(max_length=200,null=True)
    phone1=models.CharField(max_length=200,null=True)
    email1=models.CharField(max_length=200,null=True)
    pass1=models.CharField(max_length=200,null=True)
