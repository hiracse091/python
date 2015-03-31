from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kherokhata.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'kk_user.views.home', name='home'),
    url(r'^user/', include('kk_user.urls', namespace='kk_user')),
    url(r'^admin/', include(admin.site.urls)),
)
