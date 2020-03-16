import json

from django.test import TransactionTestCase, Client, TestCase
from .models import Article, ArticleType

client = Client()
class FeatureTest(TransactionTestCase):
    def setUp(self):
        ArticleType.objects.create(
            name = 'news'
        )
        ArticleType.objects.create(
            name = 'feature'
        )
        ArticleType.objects.create(
            name = 'quiz'
        )

        Article.objects.create(
            title = 'great0',
            author = 'rlagudwns0',
            thumbnail = 'slkdjf0',
            created_at = '2019-03-20',
            article_types_id = 2
        )
        Article.objects.create(
            title = 'great1',
            author = 'rlagudwns3',
            thumbnail = 'slkdjf1',
            created_at = '2019-03-20',
            article_types_id = 2
        )

    def tearDown(self):
        ArticleType.objects.all().delete()
        Article.objects.all().delete()

    def test_news_get_view(self):
        client = Client()
        response = client.get('/article/feature')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'data': list(Article.objects.values('title', 'author', 'thumbnail'))
        })

class NewsTest(TransactionTestCase):
    def setUp(self):
        ArticleType.objects.create(
            name = 'news'
        )
        ArticleType.objects.create(
            name = 'feature'
        )
        ArticleType.objects.create(
            name = 'quiz'
        )
        Article.objects.create(
            title = 'greaet3',
            author = 'rlaegudwn23s3',
            thumbnail = 'slkedj42f3',
            created_at = '2018-03-22',
            article_types = ArticleType.objects.get(id=1)
        )
        
    def tearDown(self):
        Article.objects.all().delete()
        ArticleType.objects.all().delete()

    def test_get_view2(self):
        client = Client()
        response = client.get('/article/news')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'data': list(Article.objects.values('title', 'author', 'thumbnail'))
        })