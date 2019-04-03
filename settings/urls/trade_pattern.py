from django.conf.urls import url, include
from settings.views import trade_pattern

app_name = "trade_pattern"

urlpatterns = [
    url('^create/$', trade_pattern.create, name="create"),
    url('^$', trade_pattern.list, name="list"),
    url('^edit/(?P<pk>\d+)/$', trade_pattern.edit, name="edit"),
    url('^delete/(?P<pk>\d+)/$', trade_pattern.delete, name="delete"),
]
