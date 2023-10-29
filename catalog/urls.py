from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import home, contacts, info

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('info/', info)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)