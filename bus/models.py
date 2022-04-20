from django.db import models


class Bus(models.Model):
    model = models.CharField(max_length=255)
    plate = models.CharField(max_length=8)
    destiny = models.CharField(max_length=50)
    capacity =   models.PositiveBigIntegerField(default=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.plate} - {self.model}'

    class Meta:
        ordering = ('-date_added',)


class Ticket(models.Model):
    STATUS_CHOICES = [
        ('AVATIBLE', 'Avatible'),
        ('USED', 'Used'),
        ('EXPIRED', 'Expired')
    ]

    bus = models.ForeignKey(Bus, on_delete=models.DO_NOTHING)
    departure_time = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES, default='AVATIBLE', max_length=15)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.bus.plate} - {self.status}'