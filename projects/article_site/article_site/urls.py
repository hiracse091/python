from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^articles/',include('article.urls', namespace='article')),
     (r'^accounts/',include('accounts.urls', namespace='accounts')),
    # url(r'^$', 'article_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
