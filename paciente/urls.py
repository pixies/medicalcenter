from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from paciente.views import paciente

app_name = 'paciente'

urlpatterns = [
    path('', paciente),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
