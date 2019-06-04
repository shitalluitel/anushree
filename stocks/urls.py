from django.conf.urls import url
from . import views

app_name = 'stocks'

urlpatterns = [
    url(r'^update/tyre/$', views.add_tyre_stock, name='add_tyre_stock'),
    url(r'^update/tube/$', views.add_tube_stock, name='add_tube_stock'),
    url(r'^update/$', views.create_home, name='create_home'),

    url(r'^history/$', views.history_home, name='history_home'),
    url(r'^history/tyre/$', views.list_tyre_stock, name='list_tyre_stock'),
    url(r'^history/tube/$', views.list_tube_stock, name='list_tube_stock'),
]
