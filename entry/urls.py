from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^crsid/(?P<crsid>[A-Z]+[0-9]+)/$', views.crsid, name='crsid'),
    url(r'^pk/(?P<pk>[0-9]+)/$', views.pk, name='pk'),
    url(r'^time/(?P<timestamp>[0-9.]+)$', views.time, name='time'),
]