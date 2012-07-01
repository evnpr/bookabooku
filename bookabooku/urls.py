from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'listbook.views.home', name='home'),
    url(r'^search/$', 'listbook.views.search'),
    url(r'^about/$', 'listbook.views.about', name='about'),
    # url(r'^bookabooku/', include('bookabooku.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^assets/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/evan/Downloads/web/bookabooku/static/', 'show_indexes': True}),

)
