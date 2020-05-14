from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile
from accounts import url_reset


urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^registration/$', registration, name="registration"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^password_reset_confirm/', include(url_reset)),
    url(r'^password_reset_done/', include(url_reset)),
    url(r'^password_reset_complete/', include(url_reset)),
]
