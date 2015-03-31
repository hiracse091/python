from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserType(models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    user_type = models.ForeignKey(UserType)
    emp_id = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.user.username


