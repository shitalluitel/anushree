from django.conf.urls import url
from . import views

app_name = "products"

urlpatterns = [
    url(r'^tire/create/$', views.tire_create, name="tire_create"),
    url(r'^tire/list/$', views.tire_list, name="tire_list"),
    url(r'^tire/edit/(?P<slug>[\w-]+)/$', views.tire_edit, name="tire_edit"),
    url(r'^tire/delete/(?P<slug>[\w-]+)/$', views.tire_delete, name="tire_delete"),
    url(r'^tire/undo/(?P<slug>[\w-]+)/$', views.tire_undo, name="tire_undo"),

    url(r'^tube/create/$', views.tube_create, name="tube_create"),
    url(r'^tube/list/$', views.tube_list, name="tube_list"),
    url(r'^tube/edit/(?P<slug>[\w-]+)/$', views.tube_edit, name="tube_edit"),
    url(r'^tube/delete/(?P<slug>[\w-]+)/$', views.tube_delete, name="tube_delete"),
    url(r'^tube/undo/(?P<slug>[\w-]+)/$', views.tube_undo, name="tube_undo"),
]
