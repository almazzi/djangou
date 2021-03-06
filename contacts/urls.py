from django.conf.urls import patterns, url
import contacts.views
from django.views.generic import *


urlpatterns = patterns('',
                       url(r'^$', contacts.views.ListContactView.as_view(), name='contacts-list'),
                       url(r'^new/$', contacts.views.CreateContactView.as_view(), name="contact-new"),
                       url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(), name='contact-edit'),
                       url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(), name='contact-delete'),
                       url(r'^detail/(?P<pk>\d+)/$', contacts.views.DetailContactView.as_view(), name='contact-detail'),

                       )
