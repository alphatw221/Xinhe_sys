from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
class Squad(models.Model):
    name=models.CharField(unique=True,max_length=30)

    def __str__(self):
        return str(self.name)

class Worker(models.Model):
    name=models.CharField(unique=True,max_length=30)
    id_code=models.CharField(unique=True,max_length=10)
    squad=models.ForeignKey('Squad',related_name='workers',on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.name)

class Warehouse(models.Model):

    name=models.CharField(unique=True,max_length=30)
    location=models.CharField(blank=True,null=True,max_length=30)
    squad=models.ForeignKey('Squad',related_name='ware_houses',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Product(models.Model):

    name=models.CharField(unique=True,max_length=30)
    code=models.CharField(unique=True,max_length=30,default='無')
    unit=models.CharField(default='個',max_length=5)

    def __str__(self):
        return str(self.name)

class Status(models.Model):
    name=models.CharField(unique=True,max_length=30)

    def __str__(self):
        return str(self.name)

class Type1(models.Model):
    name=models.CharField(unique=True,max_length=30)

    def __str__(self):
        return str(self.name)

class Type2(models.Model):
    name=models.CharField(unique=True,max_length=30)

    def __str__(self):
        return str(self.name)

class Region(models.Model):
    name=models.CharField(unique=True,max_length=30)

    def __str__(self):
        return str(self.name)

class Project(models.Model):
    name=models.CharField(unique=True,max_length=30)

    def __str__(self):
        return str(self.name)

class WorkSheet(models.Model):
    squad=models.ForeignKey('Squad',related_name='work_sheets',on_delete=models.DO_NOTHING)
    serial_number=models.CharField(unique=True,max_length=30)
    status=models.ForeignKey('Status',related_name='work_sheets',on_delete=models.DO_NOTHING)
    date=models.DateField()
    type1=models.ForeignKey('Type1',related_name='work_sheets',on_delete=models.DO_NOTHING)
    type2=models.ForeignKey('Type2',related_name='work_sheets',on_delete=models.DO_NOTHING)
    region=models.ForeignKey('Region',related_name='work_sheets',on_delete=models.DO_NOTHING)
    project=models.ForeignKey('Project',related_name='work_sheets',on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.serial_number)

class GetProductSheet(models.Model):

    squad=models.ForeignKey('Squad',related_name='get_product_sheets',on_delete=models.DO_NOTHING)
    date=models.DateField()

    def __str__(self):
        return str(self.id)

class UseProductSheet(models.Model):

    squad=models.ForeignKey('Squad',related_name='use_product_sheets',on_delete=models.DO_NOTHING)
    date=models.DateField()

    def __str__(self):
        return str(self.id)


class WorkSheetProducts(models.Model):

    product=models.ForeignKey('Product',related_name='work_sheet_productss',on_delete=models.DO_NOTHING)
    amount=models.IntegerField()
    work_sheet=models.ForeignKey('WorkSheet',related_name='work_sheet_productss',on_delete=models.DO_NOTHING)
    warehouse=models.ForeignKey('Warehouse',related_name='work_sheet_productss',on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)

class GetProductSheetProducts(models.Model):

    product=models.ForeignKey('Product',related_name='get_product_sheet_productss',on_delete=models.DO_NOTHING)
    amount=models.IntegerField()
    get_product_sheet=models.ForeignKey('GetProductSheet',related_name='get_product_sheet_productss',on_delete=models.DO_NOTHING)
    warehouse=models.ForeignKey('Warehouse',related_name='get_product_sheet_productss',on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return str(self.id)

class UseProductSheetProducts(models.Model):

    product=models.ForeignKey('Product',related_name='use_product_sheet_productss',on_delete=models.DO_NOTHING)
    amount=models.IntegerField()
    use_product_sheet=models.ForeignKey('UseProductSheet',related_name='use_product_sheet_productss',on_delete=models.DO_NOTHING)
    warehouse=models.ForeignKey('Warehouse',related_name='use_product_sheet_productss',on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return str(self.id)

