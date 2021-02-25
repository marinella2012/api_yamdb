from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.slug
