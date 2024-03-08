from django.db import models

class BusDriver(models.Model):
    name = models.CharField(max_length=255)
    pone_number = models.CharField(max_length=11)


    def driver_status(self,name):
        pass


class Bus(models.Model):
    bus_Id =Ticket_Id = models.CharField(max_length=12)
    capacity = models.IntegerField()
    Bus_license_plate = models.CharField(max_length=9)
    
    def Bus_status(self,name):
        pass





class Traveler(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    def Buy_tickets(self,name, phone_number):
        pass



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
     def Ticket_price_calculation(self,origin,aim,unit_price):
        pass


    def Cancel_the_ticket(self,Ticket_Id):
        pass

    def Change_of_origin_or_destination(self,origin,aim ,unit_price):
        pass



class RegularTicket(Ticket):
    baggage_allowance = models.IntegerField()

class DiscountedTicket(Ticket):
    discount_code = models.CharField(max_length=20)
    discount_amount = models.DecimalField(max_digits=6, decimal_places=2)
    def Ticket_price_calculation(self,origin,aim,unit_price,discount_code):
        pass



class Penalty(models.Model):
    traveler= models.ForeignKey(Traveler, on_delete=models.PROTECT, related_name='penalties')
    penalty_price = models.DecimalField(max_digits=6 , decimal_places=2)

    def Penalty_calculation(self, penalty_price):
        pass



class TourismMagazine(models.Model):
    TourismMagazine_id = models.CharField(max_length=12)
    datetime_created = models.DateTimeField(auto_now_add=True)


     def Publication_status(self,TourismMagazine_id,datetime_created):
        pass



class Location(models.Model):
    pass

# aaaa








# Create your models here.
