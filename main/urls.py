from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

admin.autodiscover()

import recs.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
     path('', TemplateView.as_view(template_name="recs/index.html")),
    path("db/", recs.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
]

# Only for development purposes.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
