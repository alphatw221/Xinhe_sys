from django.db import models

# Create your models here.
class Squad(models.Model):
    name=models.CharField(unique=True)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name=models.CharField(unique=True)
    id_code=models.CharField(unique=True,max_length=10)
    squad=models.ForeignKey('Squad',related_name='workers',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

class Product(models.Model):

    name=models.CharField(unique=True)
    code=models.CharField(blank=True,null=True,unique=True)
    amount=models.IntegerField()
    unit=models.CharField(default='個')
    photo=models.FileField()

    def __str__(self):
        return self.name

class Warehouse(models.Model):

    name=models.CharField(unique=True)
    location=models.CharField(blank=True,null=True)
    squad=models.ForeignKey('Squad',related_name='ware_houses',on_delete=models.CASCADE)
    products=models.ManyToManyField('Product',related_name='ware_houses',on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name

class GetProductSheet(models.Model):

    code=models.CharField(unique=True)
    products=models.ManyToManyField('Product',related_name='get_product_sheets',on_delete=models.DO_NOTHING)
    squad=models.ForeignKey('Squad',related_name='get_product_sheets',on_delete=models.DO_NOTHING)
    is_completed=models.BooleanField(default=False)
    is_blocked=models.BooleanField(default=False)
    date=models.DateField()

    def __str__(self):
        return self.code

class BlockedProject(models.Model):

    code=models.CharField(unique=True)
    get_product_sheet=models.ForeignKey('GetProductSheet',on_delete=models.DO_NOTHING,primary=True)
    date=models.DateField()

    def __str__(self):
        return self.code

class CompletedProject(models.Model):

    code=models.CharField(unique=True)
    get_product_sheet=models.ForeignKey('GetProductSheet',on_delete=models.DO_NOTHING,primary=True)
    date=models.DateField()

    def __str__(self):
        return self.code