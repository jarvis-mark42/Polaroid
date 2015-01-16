from django.conf.urls import patterns, include, url
from apps.views import home, signin, thank

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BlackHeart.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$',home),
    url(r'^signin/$',signin),
    url(r'^thanks/$',thank)
)
