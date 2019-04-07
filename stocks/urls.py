from django.conf.urls import url
from . import views

app_label = 'stocks'

urlpatterns = [
    url(r'^tire/update/$', views.add_tire_stock, name='add_tire_stock'),
    url(r'^tube/update/$', views.add_tube_stock, name='add_tube_stock'),
]
