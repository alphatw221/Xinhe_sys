from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Product)
admin.site.register(Products)
admin.site.register(Worker)
admin.site.register(Squad)
admin.site.register(Warehouse)
admin.site.register(GetProductSheet)
admin.site.register(CompletedProject)
admin.site.register(BlockedProject)
