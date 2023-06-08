
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'Tenders'
admin.site.index_title = 'Tenders Management system Admin'


urlpatterns = [
    path("", include('main.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
