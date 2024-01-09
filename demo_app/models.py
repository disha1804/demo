from django.db import models

# Create your models here.

class DEMO(models.Model):
    fname=models.CharField(max_length=50)
    age=models.CharField( max_length=50)
    marks=models.CharField(max_length=100)

    def __str__(self):
        return self.fname
    


class data(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField( max_length=50)
    marks=models.CharField( max_length=100)
    per=models.CharField(max_length=100)

    def __str__(self):
        return self.fname
    

class demo1(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    age=models.CharField(max_length=70)
    gender=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.fname


