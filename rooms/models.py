from django.db import models


class Room(models.Model):
    class RoomTypes(models.TextChoices):
        ROOM = 'room', 'Стая'
        APARTMENT = 'apartment', 'Апартамент'

    room_type = models.CharField(
        max_length=20,
        choices=RoomTypes.choices,
        default=RoomTypes.ROOM,
        verbose_name='Тип настаняване',
    )
    capacity = models.IntegerField(
        verbose_name='Капацитет', help_text='Максимален брой гости'
    )
    description = models.TextField(
        verbose_name='Описание', blank=True, null=True
    )

    def __str__(self):
        # get_room_type_display() връща 'Стая' или 'Апартамент', а не 'room'
        return f'{self.get_room_type_display()} ({self.capacity} места)'