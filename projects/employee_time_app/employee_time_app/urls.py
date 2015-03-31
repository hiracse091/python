from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'employee_time_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'employee_time.views.home', name='home'),
    url(r'^employee/', include('employee_time.urls', namespace='employee_time')),
    url(r'^admin/', include(admin.site.urls)),
)
