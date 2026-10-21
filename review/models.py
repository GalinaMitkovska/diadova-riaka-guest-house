from django.db import models

class Review(models.Model):
    class RatingChoices(models.IntegerChoices):
        FIVE = 5, 'Отлично 5 звезди'
        FOUR = 4, 'Много добро 4 звезди'
        THREE = 3, 'Добро 3 звезди'
        TWO = 2, 'Средно 2 звезди'
        ONE = 1, 'Лошо 1 звезда'

    name = models.CharField(max_length=100, verbose_name='Име')
    rating = models.IntegerField(
        choices=RatingChoices.choices,
        default=RatingChoices.FIVE,
        verbose_name='Оценка',
        help_text='Изберете оценка',
    )
    comment = models.TextField(verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.get_rating_display()}'