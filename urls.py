from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('apps.mainsite.views',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'news', name='index'),
    url(r'^index/', 'news', name='index'),
    url(r'^news/(\w+)/$', 'news', name='news')

)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

