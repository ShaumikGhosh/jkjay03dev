from django.db import models
from django.contrib.auth.models import User


class UserPost(models.Model):

    post_title = models.CharField(max_length=200, null=False, blank=False)
    post_description = models.TextField(null=False, blank=False)
    post_image = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    creation_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)

    class Meta:
        db_table = 'UserPost'
