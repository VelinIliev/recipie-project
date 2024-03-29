from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from server import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('server.api.urls')),
    # path('api-auth', include('rest_framework.urls')),
    path('account/', include('server.user_app.api.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)