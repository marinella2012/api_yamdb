from datetime import date

from django.core.exceptions import ValidationError
from django.db import models

from .category import Category
from .genre import Genre


def no_future(value):
    today = int(date.today().strftime('%Y'))
    if value > today:
        raise ValidationError('Year cannot be in the future.')


class Title(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Произведение'
    )
    year = models.PositiveIntegerField('Год выпуска',
                                       null=True,
                                       blank=True,
                                       validators=[no_future])
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
        ordering = ('-category', '-id')

    def __str__(self):
        return self.name
