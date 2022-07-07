from django.conf.urls.static import static
from django.urls import path

from photo import settings
from photosite.views import *

urlpatterns = [
    path('', home),
    path('about/', about, name='about'),
    path('albums/', albums),
    path('albums/<album>', show_album),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
