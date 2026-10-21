from django.db import models
from rooms.models import Room
from services.models import Service


class Booking(models.Model):
    guest_name = models.CharField(max_length=100, verbose_name="Име на гост")
    email = models.EmailField(verbose_name="Имейл адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефонен номер")
    number_of_guests = models.IntegerField(verbose_name="Брой гости")
    check_in = models.DateField(verbose_name="Дата на настаняване")
    check_out = models.DateField(verbose_name="Дата на напускане")

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="bookings",
        verbose_name="Избрано помещение",
    )

    services = models.ManyToManyField(
        Service,
        blank=True,
        related_name="bookings",
        verbose_name="Допълнителни услуги",
    )

    def __str__(self):
        return f"Резервация #{self.id} - {self.guest_name} ({self.room})"
