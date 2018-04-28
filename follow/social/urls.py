from django.conf.urls import url

from .views import create_post, follow_others, index, post_like, profile, signin, signout, signup, view_posts

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^createpost/$', create_post, name="create_post"),
    url(r'^followothers/$', follow_others, name="follow_others"),
    url(r'^posts/$', view_posts, name="view_posts"),
    url(r'^posts/like/(?P<post_id>[\d]*)/(?P<username>[\w-]*)/$', post_like, name="post_like"),
    url(r'^profile/(?P<slug>[\w-]*)/$', profile, name="profile"),
    url(r'^signin/$', signin, name="sign_in"),
    url(r'^signout/$', signout, name="sign_out"),
    url(r'^signup/$', signup, name="sign_up")
]
