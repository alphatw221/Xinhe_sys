from django.db import models

# Create your models here.
class Squad(models.Model):
    name=models.CharField(unique=True,max_length=30)

    def __str__(self):
        return self.name

class Warehouse(models.Model):

    name=models.CharField(unique=True,max_length=30)
    location=models.CharField(blank=True,null=True,max_length=30)
    squad=models.ForeignKey('Squad',related_name='ware_houses',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):

    name=models.CharField(unique=True,max_length=30)
    code=models.CharField(blank=True,null=True,unique=True,max_length=30)
    amount=models.IntegerField()
    unit=models.CharField(default='個',max_length=5)
    photo=models.FileField()
    warehouse=models.ForeignKey('Warehouse',related_name='products',on_delete=models.DO_NOTHING,null=True)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name=models.CharField(unique=True,max_length=30)
    id_code=models.CharField(unique=True,max_length=10)
    squad=models.ForeignKey('Squad',related_name='workers',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class GetProductSheet(models.Model):

    code=models.CharField(unique=True,max_length=30)
    products=models.ManyToManyField('Product',related_name='get_product_sheets')
    squad=models.ForeignKey('Squad',related_name='get_product_sheets',on_delete=models.DO_NOTHING)
    is_completed=models.BooleanField(default=False)
    is_blocked=models.BooleanField(default=False)
    date=models.DateField()

    def __str__(self):
        return self.code

class BlockedProject(models.Model):

    code=models.CharField(unique=True,max_length=30)
    get_product_sheet=models.ForeignKey('GetProductSheet',on_delete=models.DO_NOTHING)
    date=models.DateField()

    def __str__(self):
        return self.code

class CompletedProject(models.Model):

    code=models.CharField(unique=True,max_length=30)
    get_product_sheet=models.ForeignKey('GetProductSheet',on_delete=models.DO_NOTHING)
    date=models.DateField()

    def __str__(self):
        return self.code