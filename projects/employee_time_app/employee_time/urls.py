from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'employee_time_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'employee_time.views.home', name='home'),
    url(r'^load_data/$', 'employee_time.views.load_data', name='load_data'),
    url(r'^load_data/db/$', 'employee_time.views.load_data_into_db', name='load_data_into_db'),
    url(r'^report_data/$', 'employee_time.views.report_data', name='report_data'),
)
