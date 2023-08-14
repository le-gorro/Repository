from django.contrib import admin
from .models import Advertisements

class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_date', 'updated_date', 'auction', 'image_']
    list_filter = ['created_at', 'auction']

admin.site.register(Advertisements, AdvertisementsAdmin)
# Register your models here.
