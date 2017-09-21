from django.contrib.auth.models import User
from django.db import models


# Create your models here.

def upload_location(instance, filename):
    return 'dp/' + instance + '/' + filename


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True,
                                related_name='Profile',
                                on_delete=models.CASCADE
                                )
    mobile_number = models.PositiveIntegerField(max_length=10,
                                                blank=False
                                                )
    is_mobile_visible = models.BooleanField(default=False)
    is_email_visible = models.BooleanField(default=False)
    picture = models.ImageField(blank=True,
                                upload_to=upload_location)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user_profile',
        verbose_name = 'UserProfile',
        verbose_name_plural = 'UserProfiles'
