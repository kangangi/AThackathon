import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from dateutil import relativedelta

@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        print(text)
        print("*"*80)

        # Confirm if user exists
        # user = User.objects.filter(phone_number=phone_number)

        response = ""

        if text == "":
            response = "CON Welcome, which event would you like to attend? \n"
            response += "1. AT Hackathon"
            response += "2. WIT Event"


        elif text == "1":
            #Get event details
            response = "CON AT Hackathon next on event-date. Would you like to rsvp? \n"
            response += "1. Yes \n"
            response += "2. No \n"

        elif text == "1*2":
            #Get event details
            response = "END Thank you for using our services"

        elif text == "1*1":
            response = "The event takes place monthly. Autorenew rsvp for future events? \n"
            response += "1. Next Year\n"
            response += "2. Next six months\n"
            response += "3. Next 3 months\n"
            response += "4. Don't auto renew\n"
            
        elif text == "1*1*1":
            date = datetime.date.today()
            end_date = date.replace(year=date.year + 1)
            #create subcription f

            response = f"END Thank you for rsvping for AT Hackathon. Your subcription will end {end_date}"

        elif text == "1*1*2":
            date = datetime.date.today()
            end_date = date +  relativedelta.relativedelta(months=6) 
            #create subcription

            response = f"END Thank you for rsvping for AT Hackathon. Your subcription will end {end_date}"

        elif text == "1*1*3":
            date = datetime.date.today()
            end_date = date +  relativedelta.relativedelta(months=3) 
            #create subcription

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
            response = "The event takes place monthly. Autorenew rsvp for future events?"
            response += "1. Next Year"
            response += "2. Next six months"
            response += "3. Next 3 months"
            response += "4. Don't auto renew"
            
        elif text == "2*1*1":
            date = datetime.date.today()
            end_date = date.replace(year=date.year + 1)
            #create subcription f

            response = f"END Thank you for rsvping for WIT Event. Your subcription will end {end_date}"

        elif text == "2*1*2":
            date = datetime.date.today()
            end_date = date +  relativedelta.relativedelta(months=6) 
            #create subcription

            response = f"END Thank you for rsvping for WIT Event. Your subcription will end {end_date}"

        elif text == "2*1*3":
            date = datetime.date.today()
            end_date = date +  relativedelta.relativedelta(months=3) 
            #create subcription

            response = f"END Thank you for rsvping for AT Hackathon. Your subcription will end {end_date}"

        elif text == "2*1*4":
            response = f"END Thank you for rsvping for WIT Event happening on date"

        return HttpResponse(response)