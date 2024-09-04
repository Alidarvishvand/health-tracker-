from django.contrib.auth.models import User
from django.db import models
# from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField(max_length=200,blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null = True, blank = True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username
    