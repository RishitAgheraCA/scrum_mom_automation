import json
from email.mime.image import MIMEImage
from pathlib import Path

from django.contrib.sites.models import Site
from django.shortcuts import render
from django.utils.html import strip_tags
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
import datetime
import os

import ast

# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, 'dashboard/recording.html')

    def post(self, request):
        return render(request, 'dashboard/recording.html')

# class TaskPageView(View):
#     def get(self, request):
#         return render(request, 'dashboard/tabulator.html')


class MainPageView(View):
    def get(self,request):
        details = [
            {"name": "Sahil","email":"sahil@yopmail.com","task": "Write email series","blockers":'Ran into email series prob',"deliverables":"Automated email series"},
            {"name": "Krishna","email":"Krishna@yopmail.com", "task": "Build Free trial Form","blockers":'Error in nav bars',"deliverables":"Multi dynamic trail forms"},
            {"name": "Ritesh","email":"Ritesh@yopmail.com","task": "Write monthly Newsletter","blockers":'Content was vauge at some times',"deliverables":"Monthly news letter"},
            {"name": "Rishit","email":"Rishit@yopmail.com", "task": "Work on Home page","blockers":"To navigate the items","deliverables":"Responsive home page"},
            {"name": "Saramsa","email":"Saramsa@yopmail.com", "task": "make the layout responsive","blockers":"To use and integrate bootstrap","deliverables":"Mobile friendly view"},
        ]

        return render(request,'dashboard/display_output.html',{'data':details})

    def post(self,request):
        if request.method == "POST":
            form_data=request.POST

            data=json.loads(request.body)

            data_details=data['details']

            data_with_double_quotes = data_details.replace("'", "\"")

            parsed_data = json.loads(data_with_double_quotes)

            today = datetime.date.today()

            now = datetime.datetime.now().time()

            for p_d in parsed_data:
                recipient_email = [p_d['email']]
                subject = 'Upcoming Tasks for Today'
                from_email = 'ssaramsa@gmail.com'
                img_path = request.scheme + '://' + request.get_host()+'/static/logo.jpeg'


                context = {'username':p_d['name'],'company':"Road Runner",'img_path':img_path,'task':p_d['task'],'deliverables':p_d['deliverables'],'blockers':p_d['blockers'],'today':today,'time':now}
                email_html = render_to_string('dashboard/email_temp.html', context)

                # try:
                subject = 'Welcome to my site'
                email = EmailMultiAlternatives(subject, '', from_email,recipient_email)
                email.attach_alternative(email_html, 'text/html')

                email.send()
            return JsonResponse({'form_data':parsed_data,'msg':'Successfully sent mail to the users'})


            # except Exception as e:
            #     return JsonResponse({"details":"No data found","msg":"Something went wrong please try again !"})

class SubmitView(View):
    def get(self, request):
        return render(request, 'dashboard/home_page.html')

    def post(self, request):
        print(self.request.POST)
        import code
        code.interact(local=dict(globals(), **locals()))
        return render(request, 'dashboard/home_page.html')

class TextView(View):
    def get(self, request):
        person_text = [
            {"name": "Sahil", "email": "sahil@fakemail.com", "task": "Write email series", "Emp_num": '001',
             'Postion': 'Web Developer', 'Department': 'Web Development'},
            {"name": "Krishna", "email": "krishna@fakemail.com", "task": "Build Free trial Form", "Emp_num": '021',
             'Postion': 'Data Analyst', 'Department': 'Data Science'},
            {"name": "Ritesh", "email": "ritesh@fakemail.com", "task": "Write monthly Newsletter", "Emp_num": '031',
             'Postion': 'Project Manager', 'Department': 'Overall head'},
            {"name": "Rishit", "email": "rishit@fakemail.com", "task": "Work on Home page", "Emp_num": '031',
             'Postion': 'NLP Developer', 'Department': 'AI and Data Science'},
            {"name": "Saramsa", "email": "sam@fakemail.com", "task": "make the layout responsive", "Emp_num": '002',
             'Postion': 'Back end Web Developer', 'Department': 'Web Development'},
        ]
        return render(request, 'dashboard/person_texts.html',{'data':person_text})

    def post(self, request):
        return render(request, 'dashboard/person_texts.html')


class TaskPageView(View):
    def get(self, request):
        return render(request, 'dashboard/tabulator.html')

    def post(self,request):
        if request.method == "POST" :
            details =[
                {"name":"BOB","task":"Write email series"},
                {"name": "James","task":"Build Free trial Form"},
                {"name": "Henry","task":"Write monthly Newsletter"},
                {"name": "Raven","task":"Work on Home page"},
                {"name": "Kathy","task":"make the layout responsive"},
            ]
            return JsonResponse({'details':details})
        else:
            return HttpResponse("No data found")