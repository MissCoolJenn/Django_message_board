from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
#         ^ will not be started like test, cause its helper def
        cls.post = Post.objects.create(text='This is a test!')
#       this text will by like test data base ^
# this need cause we not use our db, for test need to create new test db

    def test_model_content(self):
#        ^ will be started like 'test' cause name begins with 'test...'
        self.assertEqual(self.post.text, 'This is a test!')
#       checking whats text in '' print out fine ^ in our page

    def test_url_name_available(self):
        responce = self.client.get('/')
        self.assertEqual(responce.status_code, 200)

    def test_homepage(self):
        responce = self.client.get(reverse('home'))
        self.assertEquals(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'home.html')
        self.assertContains(responce, 'This is a test!')
#    ^ test 3 in 1

#    def test_available_by_name(self):
#        responce = self.client.get(reverse('home'))
#        self.assertEqual(responce.status_code, 200)
#
#    def test_template_name_correct(self):
#        response = self.client.get(reverse('home'))
#        self.assertTemplateUsed(response, 'home.html')
#
#    def test_template_content(self):
#        response = self.client.get(reverse('home'))
#        self.assertContains(response, 'This is a test!')

# self contained 3 tests ^