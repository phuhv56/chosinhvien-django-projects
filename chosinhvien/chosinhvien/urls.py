from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.templatetags.static import static
from chosinhvien import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chosinhvien.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^show/', include('mysite.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'chosinhvien.views.login'),
    url(r'^accounts/auth/$', 'chosinhvien.views.auth_view'),
    url(r'^accounts/logout/$', 'chosinhvien.views.logout'),
    url(r'^accounts/loggedin/$', 'chosinhvien.views.loggedin'),
    url(r'^accounts/invalid/$', 'chosinhvien.views.invalid'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^accounts/register/$', 'chosinhvien.views.register'),
    url(r'^accounts/register_success/$', 'chosinhvien.views.register_success'),
)