# train/urls.py
from django.urls import path
from .views import predict_disease
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', predict_disease, name='predict'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
