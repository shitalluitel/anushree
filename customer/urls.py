from django.conf.urls import url
from . import views

app_name = 'customers'

urlpatterns = [
    url(r'^create/$', views.create_customer, name='create'),
    url(r'^$', views.list_customer, name='list_customer'),
    url(r'^change-password/(?P<pk>\d+)/$', views.change_customer_password, name='change_password'),
    url(r'^toggle/(?P<pk>\d+)/$', views.toggle_user_status, name='toggle_user_status'),
]
