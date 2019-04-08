from django.conf.urls import url
from . import views

app_name = 'stocks'

urlpatterns = [
    url(r'^update/tire/$', views.add_tire_stock, name='add_tire_stock'),
    url(r'^update/tube/$', views.add_tube_stock, name='add_tube_stock'),
    url(r'^update/$', views.create_home, name='create_home'),

    url(r'^history/$', views.history_home, name='history_home'),
    url(r'^history/tire/$', views.list_tire_stock, name='list_tire_stock'),
    url(r'^history/tube/$', views.list_tube_stock, name='list_tube_stock'),
]
