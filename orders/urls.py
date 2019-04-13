from django.conf.urls import url
from . import views

app_name = "orders"

urlpatterns = [
    url(r'^new/$', views.new_order_list, name='new_order_list'),
    url(r'^confirm/(?P<pk>\d+)/$', views.confirm_order, name='confirm_order'),
    url(r'^reject/(?P<pk>\d+)/$', views.reject_order, name='reject_order'),
    url(r'^add_to_cart/$', views.add_to_cart, name='add_to_cart'),
    url(r'^remove_from_cart/$', views.remove_from_cart, name='remove_from_cart'),
    url(r'^display/$', views.cart_home, name='cart_home'),
    url(r'^cart/destroy/$', views.destroy_cart, name='destroy_cart'),
]
