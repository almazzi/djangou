from django.conf.urls import patterns, include, url
import contacts
from contacts.models import Contact
from contacts.views import ListContactView
from django.contrib import admin
admin.site.register(Contact)
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'resolve_views_to_url.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^dostor/', include('dostor.urls')),


)
