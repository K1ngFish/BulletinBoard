from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

from ckeditor.fields import RichTextField


class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    TYPE = (('tanks', 'Танки'),
            ('healers', 'Хилы'),
            ('damage_dealers', 'ДД'),
            ('dealers', 'Торговцы'),
            ('guild_masters', 'Гилдмастеры'),
            ('quest_givers', 'Квестгиверы'),
            ('blacksmiths', 'Кузнецы'),
            ('tanners', 'Кожевники'),
            ('potion_masters', 'Зельевары'),
            ('spell_masters', 'Мастера заклинаний'))
    category = models.CharField(max_length=15, choices=TYPE, default='tanks', verbose_name='Категория')
    dateCreation = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=256, verbose_name = 'Заголовок')
    text = RichTextField(blank='True', null='True', verbose_name = 'Текст')
    video = models.FileField(upload_to='videos/', verbose_name='Видео', blank=True, null=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'Объявление: {self.title}'

    def get_absolute_url(self):
        return reverse('announcement_detail', args=[str(self.id)])

class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=64, verbose_name='Текст комментария', null=True, blank=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    def __str__(self):
        return f'Пользователь {self.author} прокомментировал: {self.text}'
