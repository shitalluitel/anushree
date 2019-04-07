from django.conf.urls import url
from sliderimages.api.views import SliderImageList

app_name = "api_sliderimages"

urlpatterns = [
    url(r'^$', SliderImageList.as_view(), name='api_list'),
]
