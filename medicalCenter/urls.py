from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

app_name = 'website'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls', namespace='website')),
    path('blog/', include('blog.urls', namespace='blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
