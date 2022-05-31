from django.contrib import admin

# Register your models here.
from .models import Provider, Geojson


admin.site.register(Provider)
admin.site.register(Geojson)