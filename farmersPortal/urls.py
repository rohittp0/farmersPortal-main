from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [

                  path('admin/logs/', include('admins.urls')),
                  path('admin/', admin.site.urls),
                  path('', include('accounts.urls')),
                  path('employee/', include('employees.urls')),
                  path('farmers/', include('farmers.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
