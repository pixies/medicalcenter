from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
app_name = 'website'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls', namespace='website')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('atendente/', include('conta.urls', namespace='atendente')),
    path('medico/', include('medico.urls', namespace='medico')),
    path('paciente/', include('paciente.urls', namespace='paciente')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
