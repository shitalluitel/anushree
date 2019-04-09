from django.conf.urls import url
from products.api.views import TireDetailView, TubeDetailView, TireListView, TubeListView

app_name = "api_products"

urlpatterns = [
    url(r'^tire/(?P<pk>[\d]+)/$', TireDetailView.as_view(), name='api_tire_detail'),
    url(r'^tube/(?P<pk>[\d]+)/$', TubeDetailView.as_view(), name='api_tube_detail'),
    url(r'^tire/$', TireListView.as_view(), name='api_tire_list'),
    url(r'^tube/$', TubeListView.as_view(), name='api_tube_list'),
]
