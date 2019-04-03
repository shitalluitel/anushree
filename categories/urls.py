from django.conf.urls import url
from . import views

app_name = "categories"

urlpatterns = [
    url('^create/$', views.create, name="create"),
    url('^$', views.list, name="list"),
    url('^edit/(?P<pk>\d+)/$', views.edit, name="edit"),
    url('^delete/(?P<pk>\d+)/$', views.delete, name="delete"),
    url('^undo/(?P<pk>\d+)/$', views.delete, name="delete"),
]
