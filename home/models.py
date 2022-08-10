from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    subtitle = models.CharField(max_length=50, blank=True)
    body = RichTextField()
    publish_date = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title
