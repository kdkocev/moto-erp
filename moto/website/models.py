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
    number = models.CharField(max_length=255, unique=True)
    part = models.ForeignKey('Part', on_delete=models.CASCADE)
    amount = models.IntegerField()
    date_received = models.DateField()
    date_of_expedition = models.DateField()
    date_of_delivery = models.DateField()
    completed_at = models.DateField(blank=True, null=True)
    created_at = models.DateField()

    def __str__(self):
        return self.number


class Expedition(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    amount = models.IntegerField()  # Amount of parts sent
    date_of_expedition = models.DateField()
    created_at = models.DateField()

    def __str__(self):
        return str(self.date_of_expedition)


class StoredCastings(models.Model):
    casting = models.ForeignKey('Casting', on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateField()


class MachinedParts(models.Model):
    part = models.ForeignKey('Part', on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateField()
