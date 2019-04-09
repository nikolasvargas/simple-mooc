from django.test import TransactionTestCase
from django.urls import reverse


class CourseIndexPageTests(TransactionTestCase):

    def test_course_index_page_status_code(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('courses:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_view_does_not_contains_404(self):
        response = self.client.get('/courses/')
        self.assertNotEqual(response.status_code, 404)
        self.assertNotContains(response, '<span>(404)</span>')
