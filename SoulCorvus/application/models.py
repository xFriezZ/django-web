from django.db import models


class Application(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', max_length=250)
    text_field = models.TextField('Полное описание заявки')
    date = models.DateField('Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'