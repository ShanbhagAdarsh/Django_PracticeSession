from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManger

class User(AbstractUser):

    middle_name = models.CharField(max_length=100,null=True,blank=True)
    date_of_birth = models.DateTimeField(null=True,blank=True)
    email = models.EmailField(unique=True)
    staff_user = models.BooleanField(default=False)
    student_user = models.BooleanField(default=False)
    username = models.CharField(max_length=100,null=True,blank=True)

    objects = UserManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
