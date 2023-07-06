import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from dateutil import relativedelta
from ussd.models import User, Event, Subscriptions
from flask import Flask, request, session
import africastalking
import os
import datetime
# from googleapiclient.discovery import build
import smtplib
from email.mime.text import MIMEText

@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        user = User.objects.get_or_create(phoneNumber=phone_number)[0]
        if not user.email:
            if "@" in text:
                email = text
                user.email = email
                user.save()
                email = email.split("*")[-1]
                response = f"CON type confirm to verify email {email}\n"
                response += "1.confirm\n"
                response += "2.cancel\n"

        else:
            print("here")
            if text.split('*')[-1] == 'confirm':
                print('confirm', text)
                text = "1*1"
            
            if text.split('*')[-1] == 'cancel':
                print('cancel', text)
                text = "1*2"

            if '@' in text:
                print(text)
                text = text.split('*')
                x = [value for value in text if value not in ['cancel', 'confirm']]
                y = [value for value in x if '@' not in value]
                text = '*'.join(y)
                print(text)

            
        
        

        if text == "":
            response = "CON Welcome, which event would you like to attend? \n"
            response += "1. AT Hackathon\n"
            response += "2. WIT Event\n"
        elif text == "1":
            event = Event.objects.get_or_create(eventName="AT Hackathon")[0]
            response = "CON AT Hackathon next on event-date. Would you like to rsvp? \n"
            response += "1. Yes \n"
            response += "2. No \n"
        elif text == "1*2":
            response = "END Thank you for using our services"

        elif text == "1*1":
            if not user.email:
                response = "CON Enter email\n"
            else:
                response = "CON The event takes place monthly. Autorenew rsvp for future events? \n"
                response += "1. Next Year\n"
                response += "2. Next six months\n"
                response += "3. Next 3 months\n"
                response += "4. Don't auto renew\n"
            
        elif text == "1*1*1":
            date = datetime.date.today()
            end_date = date.replace(year=date.year + 1)
            event = Event.objects.get_or_create(eventName="AT Hackathon")[0]
            subscription = Subscriptions.objects.create(
                event=event,
                startDate=date,
                endDate=end_date,
                user=user
            )

            response = f"END Thank you for rsvping for AT Hackathon. Your subcription will end {end_date}"

        elif text == "1*1*2":
            date = datetime.date.today()
            end_date = date +  relativedelta.relativedelta(months=6) 
            event = Event.objects.get_or_create(eventName="AT Hackathon")[0]
            subscription = Subscriptions.objects.create(
                event=event,
                startDate=date,
                endDate=end_date,
                user=user
            )


            response = f"END Thank you for rsvping for AT Hackathon. Your subcription will end {end_date}"

        elif text == "1*1*3":
            date = datetime.date.today()
            end_date = date +  relativedelta.relativedelta(months=3) 
            event = Event.objects.get_or_create(eventName="AT Hackathon")[0]
            subscription = Subscriptions.objects.create(
                event=event,
                startDate=date,
                endDate=end_date,
                user=user
            )

            response = f"END Thank you for rsvping for AT Hackathon. Your subcription will end {end_date}"

        elif text == "1*1*4":
            response = f"END Thank you for rsvping for AT Hackathon happening on date"


        elif text == "2":
                #Get event details
            response = "CON AT Hackathon next on event-date. Would you like to rsvp?"
            response += "1. Yes"
            response += "2. No"

        elif text == "2*2*":
            #Get event details
            response = "END Thank you for using our services"

        elif text == "2*1":
            response = "CON The event takes place monthly. Autorenew rsvp for future events?"
            response += "1. Next Year"
            response += "2. Next six months"
            response += "3. Next 3 months"
            response += "4. Don't auto renew"
            
        elif text == "2*1*1":
            date = datetime.date.today()
            end_date = date.replace(year=date.year + 1)
            event = Event.objects.get_or_create(eventName="WIT Event")[0]
            subscription = Subscriptions.objects.create(
                event=event,
                startDate=date,
                endDate=end_date,
                user=user
            )

            response = f"END Thank you for rsvping for WIT Event. Your subcription will end {end_date}"

        elif text == "2*1*2":
            date = datetime.date.today()
            end_date = date +  relativedelta.relativedelta(months=6) 
            event = Event.objects.get_or_create(eventName="WIT Event")[0]
            subscription = Subscriptions.objects.create(
                event=event,
                startDate=date,
                endDate=end_date,
                user=user
            )

            response = f"END Thank you for rsvping for WIT Event. Your subcription will end {end_date}"

        elif text == "2*1*3":
            date = datetime.date.today()
            end_date = date +  relativedelta.relativedelta(months=3) 
            event = Event.objects.get_or_create(eventName="WIT Event")[0]
            subscription = Subscriptions.objects.create(
                event=event,
                startDate=date,
                endDate=end_date,
                user=user
            )

            response = f"END Thank you for rsvping for AT Hackathon. Your subcription will end {end_date}"

        elif text == "2*1*4":
            response = f"END Thank you for rsvping for WIT Event happening on date"

        

        return HttpResponse(response)
 
