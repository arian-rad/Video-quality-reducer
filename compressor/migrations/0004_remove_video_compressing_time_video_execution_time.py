# Generated by Django 4.1.2 on 2022-10-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compressor', '0003_alter_video_main_file_alter_video_video_240_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='compressing_time',
        ),
        migrations.AddField(
            model_name='video',
            name='execution_time',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
