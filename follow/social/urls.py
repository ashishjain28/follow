from django.conf.urls import url

from .views import index, profile, signup

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^signup/$', signup, name="sign_up"),
    url(r'^profile/(?P<slug>[\w-]*)/$', profile, name="profile"),
]
