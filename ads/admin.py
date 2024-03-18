from django.contrib import admin

from ads.models import Ad


# Register your models here.

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title',)