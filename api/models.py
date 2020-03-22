from django.db import models
from django.contrib.auth.models import User


class UserPost(models.Model):

    post_title = models.CharField(max_length=200, null=False, blank=False)
    post_description = models.TextField(null=False, blank=False)
    post_image = models.ImageField(null=True, blank=True, upload_to='')
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    creation_date, update_date = models.DateField(null=False,blank=False), models.DateField(null=True, blank=True)
    creation_time, update_time = models.TimeField(null=False, blank=False), models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'UserPost'
