from django.contrib import admin
from django.urls import path
from planilha import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('templates', views.templates, name='templates_planilhas'),
    path('admin/', admin.site.urls),
    path('upload/', views.upload_planilha, name='upload_planilha'),
    path('grafico/', views.exibir_grafico, name='exibir_grafico'),
]

# Servir arquivos de mídia em ambiente de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)