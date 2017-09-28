from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import check_uploading


urlpatterns = patterns('',
                        url(r'^$', 'async_save.views.upload_file', name='upload_file'),
                        url(r'^(?P<file_id>[0-9]+)/$', check_uploading, name='check_uploading'),
                        )