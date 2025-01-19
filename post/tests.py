from django.test import TestCase
from .models import Post
from django.urls import reverse
from django.contrib.auth import get_user_model
class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='Just a test')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name=f'{post.title}'
        self.assertEqual(expected_object_name,'Just a test')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='Just a test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)

    def test_url_by_name(self):
        resp=self.client.get(reverse('home') )
        self.assertEqual(resp.status_code,200)
    
    def test_view_uses_correct_template(self):
        resp=self.client.get(reverse('home')) 
        self.assertEqual(resp.status_code ,200)
        self.assertTemplateUsed(resp,'post/home.html')  

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )         

        self.post = Post.objects.create(
            title ='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title = 'A simple title.')
        self.assertEqual(str(post),post.title)


    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','A good title')
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.postbody}','Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'Nice body content')
        self.assertTemplateUsed(response,'post/home.htnl')

    def test_post_detail_view(self):
        response = self.client.get('/1/')
        no_response=self.client.get('/1000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post/post_detail.html')
        
        
            

