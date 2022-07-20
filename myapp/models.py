from django.db import models

# Create your models here.

class signupform(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.IntegerField()

    def __str__(self):
        return self.fname

class userform(models.Model):
    title=models.CharField(max_length=100)  
    option=models.CharField(max_length=100)
    select_file=models.FileField(upload_to='myfiles')
    disc=models.TextField()




    