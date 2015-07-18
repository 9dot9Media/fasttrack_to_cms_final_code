import markdown

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.ForeignKey(User)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(null=True, blank=True)
    publish_status = models.BooleanField(default=False)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

    @property
    def content_html(self):
        return markdown.markdown(self.content)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Articles'
        ordering = ['creation_date']


class Image(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField()
    alt_text = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField()
    images = models.ManyToManyField(Image)
    description = models.TextField()
    layout = models.CharField(max_length=5,
                              choices=(
                                  ('LINK', 'Linked'),
                                  ('HORI', 'Horizontal'),
                                  ('VERT', 'Vertical')
                              ))

    def __str__(self):
        return self.name
