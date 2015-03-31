from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')
    firstname = models.CharField(max_length=100, null=True, default='')
    lastname = models.CharField(max_length=100, null=True, default='')
    emp_id = models.CharField(max_length=100, null=True, default='')
    def __str__(self):
        return self.user.username
