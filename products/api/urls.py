from django.conf.urls import url
from products.api.views import TireDetailView, TubeDetailView

app_name = "api_products"

urlpatterns = [
    url(r'^tire/(?P<pk>[\d]+)/$', TireDetailView.as_view(), name='api_list'),
    url(r'^tube/(?P<pk>[\d]+)/$', TubeDetailView.as_view(), name='api_list'),
]
