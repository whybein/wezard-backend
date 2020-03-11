from django.db import models

class News(models.Model):
    title      = models.CharField(max_length = 50)
    author     = models.CharField(max_length = 50)
    thumbnail  = models.TextField()
    content    = models.TextField()
    created_at = models.DateField()
    
    class Meta:
        db_table = 'news'

class Feature(models.Model):
    title      = models.CharField(max_length = 50)
    author     = models.CharField(max_length = 50)
    content    = models.TextField()
    created_at = models.DateField()
    
    class Meta:
        db_table = 'features'
