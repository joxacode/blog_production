from django.contrib import admin
from . import models


admin.site.register(models.Post)


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'donation')
    search_fields = ('donation', )
    list_filter = ('created_at', 'update_at')
    ordering = ('donation',)


admin.site.register(models.Project)
admin.site.register(models.Service)
admin.site.register(models.Category)
admin.site.register(models.Tool)
admin.site.register(models.SocialLink)
admin.site.register(models.ProfileData)

# Register your models here.
