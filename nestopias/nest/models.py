from django.db import models

# Create your models here.

class search(models.Model):
    def __str__(self):
        return self.name
    
class calendar(models.Model):
    def __str__(self):
        return self.name
    
class review(models.Model):
    def __str__(self):
        return self.name
    
class Booking_reminders(models.Model):
    def __str__(self):
        return self.name
    
class Booking_approval(models.Model):
    def __str__(self):
        return self.name

class Real_Time_Notification(models.Model):
    def __str__(self):
        return self.name
    
class imgage(models.Model):
    def __str__(self):
        return self.name

class history_booking(models.Model):
    def __str__(self):
        return self.name
    
class Location(models.Model):
    def __str__(self):
        return self.name
    
class Chatbot(models.Model):
    def __str__(self):
        return self.name
    
class Discount(models.Model):
    def __str__(self):
        return self.name
    
class Referral(models.Model):
    def __str__(self):
        return self.name
    
class Payment(models.Model):
    def __str__(self):
        return self.name