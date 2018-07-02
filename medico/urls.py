from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from conta.views import medico

app_name = 'medico'

urlpatterns = [
    path('', medico),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
