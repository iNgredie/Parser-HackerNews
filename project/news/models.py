from django.db import models


class News(models.Model):
    """
    Модель Новостей
    """
    title = models.CharField('Название', max_length=255)
    url = models.URLField('Ссылка')
    created = models.DateTimeField('Время создания', auto_now_add=True)

    def __str__(self):
        return self.title
