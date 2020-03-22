from django.db import models
from django.contrib.auth.models import User


class UserPost(models.Model):

    post_title = models.CharField(max_length=200, null=False, blank=False)
    post_description = models.TextField(null=False, blank=False)
    post_image = models.ImageField(null=True, blank=True, upload_to='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'UserPost'
