from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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
    path("", recs.views.index, name="index"),
    path("db/", recs.views.db, name="db"),
    path("admin/", admin.site.urls),
]

# Only for development purposes.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
