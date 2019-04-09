from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_view_does_not_contains_404(self):
        response = self.client.get('/')
        self.assertNotEqual(response.status_code, 404)
        self.assertNotContains(response, '<span>(404)</span>')


class ContactPageTests(SimpleTestCase):

    def test_contact_page_status_code(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('core:contact'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('core:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_view_does_not_contains_404(self):
        response = self.client.get('/contact/')
        self.assertNotEqual(response.status_code, 404)
        self.assertNotContains(response, '<span>(404)</span>')
