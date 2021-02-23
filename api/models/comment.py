from django.contrib.auth import get_user_model
from django.db import models

from .review import Review


class Comment(models.Model):
    review = models.ForeignKey(Review,
                               verbose_name='Отзыв',
                               on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(get_user_model(),
                               verbose_name='Комментатор',
                               on_delete=models.CASCADE,
                               related_name='comments')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True,
                                    db_index=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:15]
