from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import home, contacts, product, create_product, edit_product, delete_product, create_version

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product'),
    path('create_product/', create_product, name='create_product'),
    path('edit_product/<int:pk>/', edit_product, name='edit_product'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('create_version/<int:pk>/', create_version, name='create_version'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
