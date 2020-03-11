from django.db import models

class News(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    thumbnail = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'news'

class Feature(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    menu_id = models.IntegerField()
    class Meta:
        db_table = 'features'