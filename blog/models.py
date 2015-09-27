from django.db import models
from django.utils import timezone
from djangae.contrib import gauth

class Post(models.Model):
    """
    Description: Blog Post model
    """
    # author = models.ForeignKey('auth.User')
    author = models.ForeignKey('djangae.GaeDatastoreUser')
    title = models.CharField(max_length=200)
    text = models.TextField()
    featured_image = models.FileField(upload_to='posts/%Y/%m/%d', null=True)
    # featured_image = models.ImageField(upload_to='static/files', max_length=100, null=True)
    post_slug = models.SlugField(max_length=120)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
    	self.published_date = timezone.now()
    	self.save()

    def __str__(self):
    	return self.title
