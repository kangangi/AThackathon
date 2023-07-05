from django.db import models

# Create your models here.
class Event(models.Model):
    eventName = models.CharField(max_length=100)
    organizer = models.CharField(max_length=100)
    frequency:models.IntegerField(default=30)

    def _str_(self):
        return self.name

class User(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phoneNumber=models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Subscriptions(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nextReminder=models.DateField()
    startDate = models.DateField()
    endDate = models.DateField()

    def _str_(self):
        return self.name