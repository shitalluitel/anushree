from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^api/', include('orders.api.urls')),

                  url(r'^', include('pages.urls')),

                  url(r'^api/auth/', include('users.api.urls')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^archive/', include('settings.urls.archive')),
                  url(r'^api/customers/', include('customer.api.urls')),
                  url(r'^api/products/', include('products.api.urls')),
                  url(r'^api/sliderimages/', include('sliderimages.api.urls')),

                  url(r'^categories/', include('categories.urls')),
                  url(r'^customers/', include('customer.urls')),

                  url('^inbox/notifications/', include('notifications.urls', namespace='notifications')),

                  url(r'^order/', include('orders.urls')),

                  url(r'^products/', include('products.urls')),

                  url(r'^users/', include('users.urls')),

                  # url(r'^settings/tire-design/', include('settings.urls.tire_design')),
                  # url(r'^settings/trade-mark/', include('settings.urls.trade_mark')),
                  # url(r'^settings/trade-pattern/', include('settings.urls.trade_pattern')),
                  # url(r'^settings/type/', include('settings.urls.type')),

                  url(r'^sliderimages/', include('sliderimages.urls')),
                  url(r'^stocks/', include('stocks.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "AnuShree Traders"
admin.site.site_title = "AnuShree Traders"
