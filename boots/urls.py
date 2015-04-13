# coding=utf-8
"""
Main urls file for module
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from boots.views.demo_view import DemoView, ErrorDemo

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'boots.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', DemoView.as_view()),
                       url(r'^error/', ErrorDemo.as_view())
                       )
