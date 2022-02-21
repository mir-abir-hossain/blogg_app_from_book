from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Post

class BlogTests(TestCase):
    def setup(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@test.com',
            password = 'secret'
        )
        self.post = Post.objects.create(
            title = "a new post",
            author = self.user, 
            body = 'a nice body for new post'
        )

    def test_string_representation(self):
        post = Post(title='A sample small post')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'a new post')
        self.assertEqual(f'{self.post.body}', 'a nice body for new post')
        self.assertEqual(f'{self.post.author}', 'testuser')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'a nice body for new post')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('posts/1/')
        no_response = self.client.get('posts/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'a new post')
        self.assertTemplateUsed(response, 'post_detail.html')
