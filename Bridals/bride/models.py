from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

#Create Abstarct User Model for AUthentication using JWT and Angular

class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=300, blank=True)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=True)
    avatar = CloudinaryField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
