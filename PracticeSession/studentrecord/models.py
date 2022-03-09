from django.db import models

# Create your models here.
class studrecords(models.Model):
    usn = models.CharField(max_length=10)
    fname = models.CharField(max_length=10)
    mname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    mobno = models.IntegerField()
    emailid = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')
