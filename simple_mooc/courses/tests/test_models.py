from django.test import TestCase
from courses.models import Course


class CourseModelTestCase(TestCase):

    def test_create_course(self):
        Course.objects.create(name='test')
        assert Course.objects.all().count() == 1
