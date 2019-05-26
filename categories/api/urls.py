from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from categories.api.views import CategoryList

app_name = "categories"

urlpatterns = [
    url(r'^$', login_required()(CategoryList.as_view()), name='api_list'),
]
