"""anushree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^api/auth/', include('users.api.urls')),
                  url(r'^admin/', admin.site.urls),

                  url(r'^users/', include('users.urls')),

                  url(r'^settings/tire-design/', include('settings.urls.tire_design')),
                  url(r'^settings/trade-mark/', include('settings.urls.trade_mark')),
                  url(r'^settings/trade-pattern/', include('settings.urls.trade_pattern')),
                  url(r'^settings/type/', include('settings.urls.type')),

                  url('^inbox/notifications/', include('notifications.urls', namespace='notifications')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
