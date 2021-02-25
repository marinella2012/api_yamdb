from django.db import models

from .category import Category
from .genre import Genre


class Title(models.Model):
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField('Год выпуска',
                                       null=True,
                                       blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(Genre,
                                   db_table='genre_title',
                                   blank=True)

    class Meta:
        ordering = ['-year']

    class Meta:
        ordering = ('-category', '-id')

    def __str__(self):
        return self.name
