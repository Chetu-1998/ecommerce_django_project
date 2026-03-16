from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
    )
    
    username = models.CharField(max_length=255, unique=True)
    
    email = models.EmailField(unique=True)
    
    password = models.CharField(max_length=255, null=True, blank=True)

    contactnumber = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', "Enter a 10-digit phone number.")]
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER')

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email