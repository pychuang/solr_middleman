from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'solr_middleman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^select/', include('select_handler.urls', namespace='select_handler')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
