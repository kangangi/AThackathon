from django.db import models


# Create your models here.
class Event(models.Model):
    eventName = models.CharField(max_length=100, null=True, blank=True)
    organizer = models.CharField(max_length=100, null=True, blank=True)
    frequency = models.IntegerField(default=30, null=True, blank=True)
   # nextDate = models.DateField(null=True, blank=True)


    def _str_(self):
        return self.name

class User(models.Model):
    firstName=models.CharField(max_length=100, null=True, blank=True)
    lastName=models.CharField(max_length=100, null=True, blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    phoneNumber=models.CharField(max_length=100, null=True, blank=True)

    def _str_(self):
        return self.name

class Subscriptions(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nextReminder=models.DateField(null=True, blank=True)
    startDate = models.DateField()
    endDate = models.DateField()

    def _str_(self):
        return self.name