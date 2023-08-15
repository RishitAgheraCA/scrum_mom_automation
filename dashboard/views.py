from email.mime.image import MIMEImage
from pathlib import Path

from django.contrib.sites.models import Site
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.html import strip_tags
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from json import dumps
from datetime import datetime, timedelta


from speechtotext.task_identifier import identifyTasks
import os


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, 'dashboard/recording.html')

    def post(self, request):
        print('post called')
        return render(request, 'dashboard/recording.html')


# class TaskPageView(View):
#     def get(self, request):
#         return render(request, 'dashboard/tabulator.html')


class TableView(View):
    def get(self, request):
        details = [
            {"name": "Sahil", "email": "sahil@yopmail.com", "task": "Write email series",
             "blockers": 'Ran into email series prob', "deliverables": "Automated email series"},
            {"name": "Krishna", "email": "Krishna@yopmail.com", "task": "Build Free trial Form",
             "blockers": 'Error in nav bars', "deliverables": "Multi dynamic trail forms"},
            {"name": "Ritesh", "email": "Ritesh@yopmail.com", "task": "Write monthly Newsletter",
             "blockers": 'Content was vauge at some times', "deliverables": "Monthly news letter"},
            {"name": "Rishit", "email": "Rishit@yopmail.com", "task": "Work on Home page",
             "blockers": "To navigate the items", "deliverables": "Responsive home page"},
            {"name": "Saramsa", "email": "Saramsa@yopmail.com", "task": "make the layout responsive",
             "blockers": "To use and integrate bootstrap", "deliverables": "Mobile friendly view"},
        ]

        return render(request, 'dashboard/display_output_2.html', {'data': details})

    def post(self, request):
        print('table-view:', request.POST)

        """
            api for task identification comes here
            
            """

        details = [
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

        return render(request, 'dashboard/display_output.html', {'data': details})

        # if request.method == "POST":
        #     form_data=request.POST

        # recipient_email = ['test-f6f4dd@test.mailgenius.com']
        # subject = 'Upcoming Tasks for Today'
        # from_email = 'ssaramsa@gmail.com'
        #
        # img_path = request.scheme + '://' + request.get_host()+'/static/logo.jpeg'
        #
        # context = {'username': 'John','company':"Road Runner",'img_path':img_path,'task':'Work on email template, review mail testing sites for testing.'}
        # email_html = render_to_string('dashboard/email_temp.html', context)
        #
        # # try:
        # subject = 'Welcome to my site'
        # email = EmailMultiAlternatives(subject, '', from_email,recipient_email)
        # email.attach_alternative(email_html, 'text/html')
        #
        # email.send()
        # return JsonResponse({'form_data': form_data,'msg':'Successfully sent mail to the users'})

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


class TaskPageView(View):
    def get(self, request):
        return render(request, 'dashboard/tabulator.html')

    def post(self, request):
        if request.method == "POST":
            details = [
                {"name": "BOB", "task": "Write email series"},
                {"name": "James", "task": "Build Free trial Form"},
                {"name": "Henry", "task": "Write monthly Newsletter"},
                {"name": "Raven", "task": "Work on Home page"},
                {"name": "Kathy", "task": "make the layout responsive"},
            ]
            return JsonResponse({'details': details})
        else:
            return HttpResponse("No data found")


class SaveOutputView(View):
    def get(self, request):


        pass

    def post(self, request):
        print('save output:', request.POST)
        #save code
        #send mail
        return render('dashbord/home_page.html')

def send_mail(request,data):
    if request.method == "POST":
        form_data = request.POST

        recipient_email = ['test-f6f4dd@test.mailgenius.com']
        subject = 'Upcoming Tasks for Today'
        from_email = 'ssaramsa@gmail.com'

        img_path = request.scheme + '://' + request.get_host() + '/static/logo.jpeg'

        context = {'username': 'John', 'company': "Road Runner", 'img_path': img_path,
                   'task': 'Work on email template, review mail testing sites for testing.'}
        email_html = render_to_string('dashboard/email_temp.html', context)

        # try:
        subject = 'Welcome to my site'
        email = EmailMultiAlternatives(subject, '', from_email, recipient_email)
        email.attach_alternative(email_html, 'text/html')

        email.send()
        return None
        # except Exception as e:
        #     return JsonResponse({"details":"No data found","msg":"Something went wrong please try again !"})

class UserProfileView(View):
    def get(self, request):
        details = [
            {"name": "Sahil", "email": "sahil@yopmail.com","role":"Front End Web Developer","profile_img":"sahil.jpg"},
            {"name": "Krishna", "email": "Krishna@yopmail.com","role":"Data Scientist","profile_img":"krishna.jpg"},
            {"name": "Ritesh", "email": "Ritesh@yopmail.com","role":"NLP Engineer","profile_img":"ritesh.jpg"},
            {"name": "Rishit", "email": "Rishit@yopmail.com","role":"Team Lead","profile_img":"rishit.jpg"},
            {"name": "Saramsa", "email": "Saramsa@yopmail.com","role":"Full Stack Developer","profile_img":"saramsa.jpg"},
        ]

        return render(request, 'dashboard/user_profile.html', {'data': details})

class CalendarView(View):
    def get(self,request):
        details = [
            {"name": "Sahil", "email": "sahil@yopmail.com", "task": "Write email series",
             "blockers": 'Ran into email series prob', "deliverables": "Automated email series","deadline":"2023-07-31"},
            {"name": "Krishna", "email": "Krishna@yopmail.com", "task": "Build Free trial Form",
             "blockers": 'Error in nav bars', "deliverables": "Multi dynamic trail forms","deadline":"2023-08-01"},
            {"name": "Ritesh", "email": "Ritesh@yopmail.com", "task": "Write monthly Newsletter",
             "blockers": 'Content was vauge at some times', "deliverables": "Monthly news letter","deadline":"2023-08-02"},
            {"name": "Rishit", "email": "Rishit@yopmail.com", "task": "Work on Home page",
             "blockers": "To navigate the items", "deliverables": "Responsive home page","deadline":"2023-08-02"},
            {"name": "Saramsa", "email": "Saramsa@yopmail.com", "task": "make the layout responsive",
             "blockers": "To use and integrate bootstrap", "deliverables": "Mobile friendly view","deadline":"2023-08-07"},
        ]

        result = {'Krishna': 'Presentation,Report,3,Citation','Alex': 'Coding part of the project,Documentation,2,No significant challenges yet.'}

        check = []

        for k,v in result.items():
            temp_dict = {}
            temp_result = v.split(',')
            temp_dict['name']=k
            temp_dict['completed_task'] = temp_result[0]
            temp_dict['ongoing_task'] =temp_result[1]
            offset = int(temp_result[2])

            days_req = self.get_date_offset(offset)

            temp_dict['days_req']= days_req
            temp_dict['blockers'] = temp_result[3]


            check.append(temp_dict)

        dataJSON = dumps(check)
        # return HttpResponse(dataJSON)
        return render(request, 'dashboard/calendar_task.html', {'data': check})

    def get_date_offset(self,offset):
        try:
            # Get today's date
            today = datetime.now().date()

            # Calculate the new date by adding the offset
            new_date = today + timedelta(days=offset)

            # Format the new date as a string
            new_date_str = new_date.strftime("%Y-%m-%d")

            return new_date_str
        except Exception as e:
            return str(e)
