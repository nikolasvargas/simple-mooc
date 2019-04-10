from django.test import TestCase
from courses.models import Course
from faker import Faker


FAKE = Faker()


class CourseModelTestCase(TestCase):

    def setUp(self):
        Course.objects.create(
            name=FAKE.name()
        )

    def test_create_course(self):
        assert Course.objects.all().count() == 1
