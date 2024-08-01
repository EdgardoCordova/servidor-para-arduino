from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('ONsettings/', include('ONsettings.urls',namespace='ONsettings')),
    path('api-auth/', include('rest_framework.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)