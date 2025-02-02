from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static


def home(request):
    return HttpResponse("Welcome to the Coffee Leaf Disease Detection System!")

urlpatterns = [

   # path('api/', include('api.urls')),  # API endpoints
    path('', home, name='home'),  # Add this line for the root URL
    path('admin/', admin.site.urls),
    path('predict/', include('predict.urls')),
    path('train/', include('train.urls')),
    #path('media/<path:path>/', some_media_view),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
