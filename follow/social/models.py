from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


from itertools import count
# Create your models here.


def upload_location(instance, filename):
    return str(instance.user.username) + '/dp/' + filename


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True,
                                related_name='Profile',
                                on_delete=models.CASCADE
                                )
    mobile_number = models.CharField(max_length=10, blank=False)
    is_mobile_visible = models.BooleanField(default=False)
    is_email_visible = models.BooleanField(default=False)
    image = models.ImageField(blank=True,
                              upload_to=upload_location)
    slug = models.SlugField(unique=True)
    # friends = models.ManyToManyField("self", blank=True)
    # friend_requests_sent = models.ManyToManyField("self", blank=True)
    # friend_requests_received = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if self.slug == "":
            slug = slugify(self.user.username)
            for x in count(1):
                if not Profile.objects.filter(slug=slug).exists():
                    break
                slug = '%s-%d' % (slug, x)

                # slug = slug + '-1'
                # exists = Profile.objects.filter(slug=slug).exists()
                # while exists:
                #     parts = slug.split('-')
                #     number = int(parts[-1]) + 1
                #     slug = parts[:-1] + str(number)
                #     exists = Profile.objects.filter(slug=slug).exists()
            self.slug = slug
            # print(self.slug)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        db_table = 'user_profile'
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'


# def pre_save_profile(sender, instance, *args, **kwargs):
#     slug = slugify(instance.user.username)
#     exists = Profile.objects.filter(slug=slug).exists()
#     if exists:
#         slug = slug+'-1'
#         exists = Profile.objects.filter(slug=slug).exists()
#         while exists:
#             parts = slug.split('-')
#             number = int(parts[-1]) + 1
#             slug = parts[:-1] + str(number)
#             exists = Profile.objects.filter(slug=slug).exists()
#     instance.slug = slug


# pre_save.connect(pre_save_profile, sender=Profile)


def post_upload_location(instance, filename):
    return str(instance.user.username) + '/posts/' + filename


class Post(models.Model):
    content = models.TextField(max_length=200, blank=False)
    post_image = models.ImageField(blank=True,
                                   upload_to=post_upload_location)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='Post')
    post_date = models.DateTimeField(auto_now_add=True)
    likes_count = models.PositiveIntegerField(default=0)
    likers = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.content
