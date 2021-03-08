from django.db import models
from django.utils import timezone


class Part(models.Model):
    number = models.CharField(max_length=255, unique=True)
    price_total = models.DecimalField(decimal_places=2, max_digits=10)
    price_machining = models.DecimalField(decimal_places=2, max_digits=10)
    casting = models.ForeignKey('Casting', on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Casting(models.Model):
    number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.number


class Order(models.Model):
    number = models.CharField(max_length=255, unique=True)
    part = models.ForeignKey('Part', on_delete=models.CASCADE)
    amount = models.IntegerField()
    date_received = models.DateField()
    date_of_expedition = models.DateField()
    date_of_delivery = models.DateField()
    completed_at = models.DateField(blank=True, null=True)
    created_at = models.DateField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamp '''
        if not self.id:
            self.created = timezone.now()
        return super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.number
