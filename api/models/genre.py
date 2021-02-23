from django.db import models

from .title import Title


class Genre(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    titles = models.ManyToManyField(Title, db_table='genre_title')

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.slug
