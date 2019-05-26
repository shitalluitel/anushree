from django.conf.urls import url
from django.contrib.auth.decorators import permission_required

from customer.api.views import CustomerDetailView

app_name = "api_customers"

urlpatterns = [
    # url(
    #     r'^detail/(?P<pk>[\d]+)/$',
    #     permission_required('customer.detail_customer', raise_exception=True)(CustomerDetailView.as_view()),
    #     name='api_customer_detail'
    # ),
    url(
        r'^detail/(?P<pk>[\d]+)/$',
        CustomerDetailView.as_view(),
        name='api_customer_detail'
    ),
]
