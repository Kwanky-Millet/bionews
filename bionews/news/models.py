from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(unique=True)
    url_to_image = models.URLField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title

