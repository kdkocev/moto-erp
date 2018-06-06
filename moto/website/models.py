from django.db import models


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
    order_number = models.CharField(max_length=255, unique=True)
    part = models.ForeignKey('Part', on_delete=models.CASCADE)
    amount = models.IntegerField()
    date_received = models.DateField()
    date_of_expedition = models.DateField()
    date_of_delivery = models.DateField()
    completed_at = models.DateField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_number
