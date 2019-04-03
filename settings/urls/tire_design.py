from django.conf.urls import url, include
from settings.views import tire_design

app_name = "tire_design"

urlpatterns = [
    url('^create/$', tire_design.create, name="create"),
    url('^$', tire_design.list, name="list"),
    url('^edit/(?P<pk>\d+)/$', tire_design.edit, name="edit"),
    url('^delete/(?P<pk>\d+)/$', tire_design.delete, name="delete"),
]
