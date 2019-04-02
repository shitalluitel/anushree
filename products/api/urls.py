from django.conf.urls import url
from products.api.views import ProductList

app_name = "products"

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', ProductList.as_view(), name='api_list'),
]
