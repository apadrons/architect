from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'core'
urlpatterns = [
    path("home/", views.core_home, name="home"),
    path("about/", views.core_about, name="about"),
    path("contact/", views.core_contact, name="contact"),
    path("gallery/", views.core_gallery, name="gallery"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)