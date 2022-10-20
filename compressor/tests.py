from django.test import TestCase
import redis
from shutil import which


class TestCompressor(TestCase):
    def setUp(self):
        pass

    def test_if_redis_is_available(self):
        r = redis.Redis(host="127.0.0.1", port="6379")
        result = r.ping()
        self.assertEqual(result, True)

    def test_if_ffmpeg_is_installed(self):
        self.assertIsNotNone(which('ffmpeg'))
