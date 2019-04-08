from django.conf.urls import url

from customer.api.views import CustomerDetailView

app_name = "api_customers"

urlpatterns = [
    url(r'^detail/(?P<pk>[\d]+)/$', CustomerDetailView.as_view(), name='api_customer_detail'),
]
