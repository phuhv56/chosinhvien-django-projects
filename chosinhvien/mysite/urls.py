# __author__ = 'Der Kaiser'
from django.conf import settings

from django.conf.urls import include, url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.templatetags.static import static

urlpatterns = patterns(
    '',
    url(r'^all/$', 'mysite.views.show_all'),
    url(r'^product/(?P<product_slug>.*)/$', 'mysite.views.product_detail'),
    url(r'^create/$', 'mysite.views.create'),
    url(r'^search/$', 'mysite.views.search_product'),
)