from django.conf.urls import url

from .views import create_post, index, profile, signin, signup

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^createpost/$', create_post, name="create_post"),
    url(r'^profile/(?P<slug>[\w-]*)/$', profile, name="profile"),
    url(r'^signin/$', signin, name="sign_in"),
    url(r'^signup/$', signup, name="sign_up")
]
