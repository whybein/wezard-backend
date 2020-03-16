from django.db         import models
from django.utils.text import slugify

class ArticleType(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'article_types'

class Article(models.Model):
    title      = models.CharField(max_length = 200)
    author     = models.CharField(max_length = 50)
    thumbnail  = models.TextField()
    content    = models.TextField()
    created_at = models.DateField()
    # slug       = models.SlugField(unique = True)
    article_types = models.ForeignKey('ArticleType', on_delete = models.CASCADE, null=True)
    is_main    = models.BooleanField(default=False)

    # def save(self, *args, **kwargs): 
    #     self.slug = slugify(self.title)
    #     super(News, self).save(*args, **kwargs)
    
    class Meta:
        db_table = 'articles'
