from django.db import models

from .title import Title


class Genre(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    title = models.ManyToManyField(Title)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title'], name='unique_title'),
        ]

    def __str__(self):
        return self.slug
