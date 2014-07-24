import datetime
from pyquery import PyQuery
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from posts.models import Post


class PostMethodTests(TestCase):
    def test_recently_published(self):
        future_post = Post(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertFalse(future_post.is_published_recently())
        old_post = Post(pub_date=timezone.now() - datetime.timedelta(days=30))
        self.assertFalse(old_post.is_published_recently())
        recent_post = Post(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertTrue(recent_post.is_published_recently())

    def test_preprocess(self):
        post_text = '<iframe src="//www.youtube.com/embed/mY5jXUW3tkk" frameborder="0" height="360" width="640"></iframe>'
        post = Post(text=post_text)
        pq = PyQuery(post.processed_text)
        self.assertEquals(len(pq('.responsive-video')), 1)


def create_post(text, days):
    return Post.objects.create(text=text,
                               pub_date=timezone.now() + datetime.timedelta(days=days))

class PostViewTests(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser('admin', 'admin@test.ru',
                                                        'password')

    def test_index_view(self):
        response = self.client.get(reverse('posts:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available")
        self.assertQuerysetEqual(response.context['last_posts'], [])
        # past post must be shown
        create_post(text="Past post", days=-15)
        response = self.client.get(reverse('posts:index'))
        self.assertQuerysetEqual(response.context['last_posts'], ['<Post: Past post>'])
        # future posts must not be shown
        create_post(text="Future post", days=15)
        response = self.client.get(reverse('posts:index'))
        self.assertQuerysetEqual(response.context['last_posts'], ['<Post: Past post>'])
        # but an admin can see all posts
        r = self.client.login(username='admin', password='password')
        self.assertTrue(r)
        response = self.client.get(reverse('posts:index'))
        self.assertQuerysetEqual(response.context['last_posts'],
                                 ['<Post: Future post>', '<Post: Past post>'])


class PostIndexDetailTests(TestCase):
    def test_detail_view(self):
        future_post = create_post("Future post", days=10)
        old_post = create_post("Old post", days=-10)
        response = self.client.get(reverse('posts:detail', args=(future_post.id, )))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse('posts:detail', args=(old_post.id, )))
        self.assertContains(response, old_post.text, status_code=200)
