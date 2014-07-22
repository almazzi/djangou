from django.conf.urls import patterns, url
from django.views.generic import *
import dostor.views



urlpatterns = patterns('',
                       url(r'^list/$', dostor.views.DostorListView.as_view(), name='dos-list'),
                       url(r'^new/$', dostor.views.DostorCreateView.as_view(), name='dos-create'),
                       url(r'^edit/(?P<pk>\d+)', dostor.views.DostorUpdateView.as_view(), name='dos-edit'),
                       url(r'detail/(?P<pk>\d+)', dostor.views.DostorDetailView.as_view(), name='dos-detail'),
                       url(r'^delete/(?P<pk>\d+)', dostor.views.DostorDeleteView.as_view(), name='dos-delete'),
                       )
