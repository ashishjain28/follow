from django.conf.urls import url

from .views import create_post, index, profile, signin, signout, signup, view_posts

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^createpost/$', create_post, name="create_post"),
    url(r'^posts/$', view_posts, name="view_posts"),
    url(r'^profile/(?P<slug>[\w-]*)/$', profile, name="profile"),
    url(r'^signin/$', signin, name="sign_in"),
    url(r'^signout/$', signout, name="sign_out"),
    url(r'^signup/$', signup, name="sign_up")
]
