from django.db         import models

class ArticleType(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'article_types'

class Article(models.Model):
    title         = models.CharField(max_length = 200)
    author        = models.CharField(max_length = 50)
    thumbnail     = models.TextField()
    content       = models.TextField()
    created_at    = models.DateField()
    article_types = models.ForeignKey('ArticleType', on_delete = models.CASCADE, null=True)

    class Meta:
        db_table = 'articles'
