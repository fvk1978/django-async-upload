from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                        (r'^file/', include('async_save.urls')),
                        url(r'^admin/', include(admin.site.urls)),
                        )
