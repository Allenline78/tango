from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name  # __unicode__(self): for python2


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    # __unicode__(self): for python2
    def __str__(self):
        return self.title


def popCategory(name):
    category = Category.objects.get_or_create(
        name=name)[0]
    return category


def popPage(category, title, url, views=0):
    page = Page.objects.get_or_create(category=category,
                                      title=title, url=url, views=views)[0]
    page.save()
