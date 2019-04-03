from django.conf.urls import url, include
from settings.views import type

app_name = "type"

urlpatterns = [
    url('^create/$', type.create, name="create"),
    url('^$', type.list, name="list"),
    url('^edit/(?P<pk>\d+)/$', type.edit, name="edit"),
    url('^delete/(?P<pk>\d+)/$', type.delete, name="delete"),
]
