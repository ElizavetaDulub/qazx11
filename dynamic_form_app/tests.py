from django.test import TestCase
from django.urls import reverse
from .models import FormData


class FormTests(TestCase):
    def setUp(self):
        FormData.objects.all().delete()

    def test_form_view_get(self):
        response = self.client.get(reverse('form'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Введите имена участников')

    def test_form_view_post_creates_data(self):
        response = self.client.post(reverse('form'), data={
            'name0': 'Аня',
            'name1': 'Игорь'
        })
        self.assertRedirects(response, reverse('members_list'))
        self.assertEqual(FormData.objects.count(), 1)
        data = FormData.objects.first().data
        self.assertIn('name0', data)
        self.assertEqual(data['name0'], 'Аня')

    def test_form_rejects_empty_names(self):
        response = self.client.post(reverse('form'), data={
            'name0': '   ',
            'name1': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Введите хотя бы одно имя.')
        self.assertEqual(FormData.objects.count(), 0)

    def test_members_list_view(self):
        FormData.objects.create(data={'name0': 'Аня', 'name1': 'Игорь'})
        response = self.client.get(reverse('members_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Список участников')
        self.assertContains(response, 'Аня')
        self.assertContains(response, 'Игорь')
