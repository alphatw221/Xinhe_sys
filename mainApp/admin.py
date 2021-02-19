from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Product)
admin.site.register(Worker)
admin.site.register(Squad)
admin.site.register(Warehouse)
admin.site.register(WorkSheet)
admin.site.register(UseProductSheet)
admin.site.register(GetProductSheet)
admin.site.register(WorkSheetProducts)
admin.site.register(UseProductSheetProducts)
admin.site.register(GetProductSheetProducts)
admin.site.register(Type1)
admin.site.register(Type2)
admin.site.register(Region)
admin.site.register(Project)
admin.site.register(Status)
