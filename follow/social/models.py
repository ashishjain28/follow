from django.contrib.auth.models import User
from django.db import models


# Create your models here.

def upload_location(instance, filename):
    return instance + '/dp/' + filename


class Profile(models.Model):
    user = models.OneToOneField('User', primary_key=True,
                                related_name='Profile',
                                on_delete=models.CASCADE
                                )
    mobile_number = models.PositiveIntegerField(blank=False)
    is_mobile_visible = models.BooleanField(default=False)
    is_email_visible = models.BooleanField(default=False)
    image = models.ImageField(blank=True,
                              upload_to=upload_location)
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user_profile',
        verbose_name = 'UserProfile',
        verbose_name_plural = 'UserProfiles'


def post_upload_location(instance, filename):
    return instance.user.username + '/posts/' + filename


class Post(models.Model):
    content = models.TextField(max_length=200, blank=False)
    post_image = models.ImageField(blank=True,
                                   upload_to=post_upload_location)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    likes_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content + 'by' + self.user.username
