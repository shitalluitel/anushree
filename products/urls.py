from django.conf.urls import url
from . import views

app_name = "products"

urlpatterns = [
    url(r'^tyre/create/$', views.tyre_create, name="tyre_create"),
    url(r'^tyre/list/$', views.tyre_list, name="tyre_list"),
    url(r'^tyre/edit/(?P<slug>[\w-]+)/$', views.tyre_edit, name="tyre_edit"),
    url(r'^tyre/delete/(?P<slug>[\w-]+)/$', views.tyre_delete, name="tyre_delete"),
    url(r'^tyre/undo/(?P<slug>[\w-]+)/$', views.tyre_undo, name="tyre_undo"),

    url(r'^tube/create/$', views.tube_create, name="tube_create"),
    url(r'^tube/list/$', views.tube_list, name="tube_list"),
    url(r'^tube/edit/(?P<slug>[\w-]+)/$', views.tube_edit, name="tube_edit"),
    url(r'^tube/delete/(?P<slug>[\w-]+)/$', views.tube_delete, name="tube_delete"),
    url(r'^tube/undo/(?P<slug>[\w-]+)/$', views.tube_undo, name="tube_undo"),

    url(r'^home/$', views.product_home, name='product_home'),
]
