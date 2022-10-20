from django.core.validators import FileExtensionValidator
from django.db import models


class Video(models.Model):
    main_file = models.FileField(upload_to='videos', validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    video_240 = models.FileField(null=True, blank=True,  validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    video_360 = models.FileField(null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    execution_time = models.PositiveIntegerField(null=True, blank=True, help_text="Total execution time in second")

    def __str__(self):
        return self.main_file.name
