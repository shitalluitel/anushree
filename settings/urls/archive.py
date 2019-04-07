from django.conf.urls import url, include
from settings.views import archive

app_name = "archive"

urlpatterns = [
    url('^$', archive.archive_home, name="home"),
    url('^product/$', archive.product_archive_home, name="product_archive_home"),
    url('^tire/list/$', archive.tire_archive, name="tire_archive"),
    url('^tube/list/$', archive.tube_archive, name="tube_archive"),
    url('^categories/list/$', archive.category_archive, name="category_archive"),
]
