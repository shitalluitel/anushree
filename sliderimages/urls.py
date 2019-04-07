from django.conf.urls import url
from . import views

app_name = "sliderimages"

urlpatterns = [
    url(r'^$', views.list_slider_image, name='list'),
    url(r'^create/$', views.create_slider_image, name='create'),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.edit_slider_image, name='edit'),
    url(r'^delete/(?P<slug>[\w-]+)/$', views.delete_slider_image, name='delete'),
]
