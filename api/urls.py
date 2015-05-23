from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^gbs$', views.index, name='index'),
    url(r'^xgbs$', views.index, { 'interpreter' : 'xgbs' }, name='index'),
)