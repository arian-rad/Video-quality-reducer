import os, subprocess
from subprocess import Popen
from celery import shared_task
from .models import Video


@shared_task
def reduce_quality_to_240(video_id):
    video_obj = Video.objects.get(id=video_id)
    filename = video_obj.main_file.file.name.split('.')[0]
    quality_dict = {
        '240': '426:240',
        '360': '640:360'
    }

    for key in quality_dict.keys():
        # Absolute file path
        path_to_file = video_obj.main_file.file.name.replace(str(video_obj.main_file), '')
        new_filename = f'{filename}-{key}.mp4'

        os.system(f'ffmpeg -i {video_obj.main_file.file.name} -vf  scale={quality_dict[key]} {new_filename}')
        new_filename = new_filename.replace(path_to_file, '')
        if key == '240':
            video_obj.video_240.name = new_filename
        else:
            video_obj.video_360.name = new_filename
        video_obj.save()

