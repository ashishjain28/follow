from django.conf.urls import url

from .views import create_post, index, profile, signup

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^signup/$', signup, name="sign_up"),
    url(r'^profile/(?P<slug>[\w-]*)/$', profile, name="profile"),
    url(r'^createpost/$', create_post, name="create_post")
]
