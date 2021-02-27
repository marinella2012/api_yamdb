from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Категория'
    )
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.slug
