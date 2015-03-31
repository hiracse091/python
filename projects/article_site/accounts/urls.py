from django.conf.urls import patterns , include, url

urlpatterns = patterns('',
    url(r'^login/$','accounts.views.login'),
    url(r'^auth/$','accounts.views.auth_view'),
    url(r'^logout/$','accounts.views.logout'),
    url(r'^loggedin/$','accounts.views.loggedin'),
    url(r'^invalid/$','accounts.views.invalid_login'),
    url(r'^register/$','accounts.views.register_user'),
    url(r'^register_success/$','accounts.views.register_success'),
)