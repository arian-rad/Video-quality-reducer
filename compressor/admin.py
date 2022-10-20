from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    readonly_fields = ('video_240', 'video_360', 'execution_time')
