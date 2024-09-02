from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, null=True)
    no_of_guests = models.IntegerField(default=0)
    bookingdate = models.DateTimeField()

class Menu(models.Model):
    title = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inventory= models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}:{str(self.price)}'