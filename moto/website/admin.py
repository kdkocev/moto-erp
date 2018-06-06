from django.contrib import admin

from moto.website.models import Part, Order, Casting


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Casting)
class CastingAdmin(admin.ModelAdmin):
    pass
