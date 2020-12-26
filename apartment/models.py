from django.db import models


class Bill(models.Model):
    price = models.DecimalField(max_digits=15, decimal_places=5)
    repayment_date = models.DateField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        abstract = True


class PowerBill(Bill):
    CHOICE = [
        ('water', 'Water'),
        ('gas', 'Gas'),
        ('electricity', 'Electricity')
    ]
    type = models.CharField(max_length=11, choices=CHOICE)
    counter_number = models.DecimalField(max_digits=15, decimal_places=3)
