from django.conf.urls import url
from . import views

app_name = "categories"

urlpatterns = [
    url(r'^create/$', views.create, name="create"),
    url(r'^$', views.list, name="list"),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.edit, name="edit"),
    url(r'^delete/(?P<slug>[\w-]+)/$', views.delete, name="delete"),
    url(r'^undo/(?P<slug>[\w-]+)/$', views.undo, name="undo"),
]
