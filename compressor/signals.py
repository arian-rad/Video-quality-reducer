from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Video
from .tasks import reduce_quality_to_240
import time
from django.db import transaction


@receiver(post_save, sender=Video)
def reduce_quality(sender, instance, created, **kwargs):
    """
    Calls two celery tasks to reduce the quality of the given video
    """
    if created:
        # Store start time
        start_time = time.time()

        # Reduction Process
        reduce_quality_to_240.delay(instance.id)
        # reduce_quality_to_360.delay(instance.id)

        # Store end time
        end_time = time.time() - start_time
        instance.execution_time = end_time

        instance.save()
