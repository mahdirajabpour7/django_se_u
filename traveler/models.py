from django.db import models


class Bus(models.Model):
    bus_Id =Ticket_Id = models.CharField(max_length=12)
    capacity = models.IntegerField()
    Bus_license_plate = models.CharField(max_length=9)




class Traveler(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


class Address(models.Model):
    traveler = models.OneToOneField(Traveler, on_delete=models.CASCADE, primary_key=True)
    province = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

class Ticket(models.Model):
    Ticket_Id = models.CharField(max_length=12)
    traveler = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    origin = models.CharField(max_length=22)
    aim  = models.CharField(max_length=22)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    seat_number = models.CharField(max_length=2)
    datetime_created = models.DateTimeField(auto_now_add=True)


class RegularTicket(Ticket):
    baggage_allowance = models.IntegerField()

class DiscountedTicket(Ticket):
    discount_code = models.CharField(max_length=20)
    discount_amount = models.DecimalField(max_digits=6, decimal_places=2)



class Penalty(models.Model):
    traveler= models.ForeignKey(Traveler, on_delete=models.PROTECT, related_name='penalties')
    penalty_price = models.DecimalField(max_digits=6 , decimal_places=2)


class TourismMagazine(models.Model):
    TourismMagazine_id = models.CharField(max_length=12)
    datetime_created = models.DateTimeField(auto_now_add=True)










# Create your models here.
