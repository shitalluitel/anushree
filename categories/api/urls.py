from django.conf.urls import url
from categories.api.views import CategoryList

app_name = "categories"

urlpatterns = [
    url(r'^$', CategoryList.as_view(), name='api_list'),
]
