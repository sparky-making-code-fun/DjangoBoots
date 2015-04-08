# coding=utf-8
"""
Main urls file for module
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import DemoView, ErrorDemo

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'boots.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^error/', ErrorDemo.as_view()),
                       url(r'', DemoView.as_view()),
                       )
