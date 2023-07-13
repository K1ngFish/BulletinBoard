from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField

class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, verbose_name = 'Заголовок')
    # text = RichTextField()

class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)
