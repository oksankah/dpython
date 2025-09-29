from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView, ArticleCategoryList

class HomeTests(TestCase):

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)

    def test_home_view_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'index.html')


class CategoryViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        from .models import Category
        Category.objects.create(category='Innovations', slug='innovations')

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('innovations',))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
