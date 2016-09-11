from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'curso_ead.core.views.home', name='home'), 
    url(r'^contato/$', 'curso_ead.core.views.contato', name='contato'),
    url(r'^admin/', include(admin.site.urls)),
)
