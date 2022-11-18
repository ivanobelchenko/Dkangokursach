from django.db import models
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def user_lvl(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s Уровень не должен быть отрицательным'),
            params={'value': value},
)   


class Author(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=25)
    discrition = models.TextField(verbose_name='Об авторе')
    amount = models.FloatField(verbose_name='Новостей написано')
    on_portal = models.TimeField(verbose_name='На ресурсе с ')

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        
        
class News(models.Model):
    title = models.CharField(verbose_name='Название', max_length=25)
    description = models.TextField(verbose_name='Описание')
    author = models.ManyToManyField(Author,verbose_name='Автор новости')
    likes = models.IntegerField(verbose_name='Лайков')

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class User(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=25)
    likes = models.IntegerField(verbose_name='Количество лайков')
    favorite_news = models.ManyToManyField(News,verbose_name='Любимая новость')
    timespend = models.TimeField(verbose_name='Последний раз был на портале')
    favorite_author = models.ManyToManyField(Author,verbose_name='Любимый Автор')
    level = models.IntegerField(verbose_name='Уровень пользователя', validators=[user_lvl])
    

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


