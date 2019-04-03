from django.conf.urls import url, include
from settings.views import trade_mark

app_name = "trade_mark"

urlpatterns = [
    url('^create/$', trade_mark.create, name="create"),
    url('^$', trade_mark.list, name="list"),
    url('^edit/(?P<pk>\d+)/$', trade_mark.edit, name="edit"),
    url('^delete/(?P<pk>\d+)/$', trade_mark.delete, name="delete"),
]
