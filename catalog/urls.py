from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import home, contacts,  product

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('product/<int:pk>/', product, name='product_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)