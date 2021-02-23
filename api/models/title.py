from django.db import models

from .category import Category


class Title(models.Model):
    name = models.TextField(max_length=50)
    year = models.PositiveIntegerField('Год выпуска')
    description = models.TextField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-year']

    def __str__(self):
        return self.name
