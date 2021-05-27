from django.contrib import admin

# Register your models here.

from recs.models import Topic, Entry, Companies, Jobs

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Companies)
admin.site.register(Jobs)
