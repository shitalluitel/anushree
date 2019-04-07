from django.conf.urls import url
from products.api.views import TireDetailView

app_name = "api_products"

urlpatterns = [
    url(r'^tube/(?P<pk>[\d]+)/$', TireDetailView.as_view(), name='api_list'),
]
