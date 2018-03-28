from django.conf import settings
from django.test import TestCase


class AnyTest(TestCase):
    def test_fail(self):
        self.assertEqual(2,3)