
from django.db import models


class Service(models.Model):
    class ServiceType(models.TextChoices):
        TRANSPORT = "transport", "Транспорт"
        HORSES = "horses", "Разходка с коне"
        FOOD = "food", "Храна и кетъринг"
        OTHER = "other", "Друга услуга"

    service_type = models.CharField(
        max_length=30,
        choices=ServiceType.choices,
        default=ServiceType.OTHER,
        verbose_name="Тип услуга",
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Име на услугата",
        help_text="Напр. Транспорт или Разходка с коне в планината",
    )
    description = models.TextField(
        verbose_name="Описание", blank=True, null=True
    )

    def __str__(self):
        return f"{self.get_service_type_display()}: {self.name}"