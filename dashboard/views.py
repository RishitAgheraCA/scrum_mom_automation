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
        print('requesttttttttttttttttttttttt',request.POST)
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
        """< QueryDict: {'csrfmiddlewaretoken': ['7WpzZTVu2w7LXtXE8o7yYBwzcdVeUlCk3gD9RYJe9fC63Q2gO1tEFcQspZKY4lU7'],
                      'task_1': ['I have done Login page development. And I will deliver
                                 the signup module this Friday.I have no blocker.'],
                      'name_1': ['John'],
                       'task_2': ['I
                                 have Model training done.And I will deliver the Model Evaluation.I am facing
                                 difficulties in C
                                 hart creation.'],
                       'name_2': ['Peter'],
                       'task_3': ['I have done speaker diarization.And
                                 I will deliver the Task identification module in two days.I am facing
                                 challenges in deployment.'],
                       'name_3': ['Sara']}>
                                                                              
            api for task identification comes here
            
            """
        names_and_contexts = {
            "Krishna": "Hello, my name is Krishna. I completed the presentation. I am working on a report which is expected to be completed in 3 days. I have experienced some challenges in citation in report",
            "Alex": "Hi, I'm Alex. I have finished the coding part of the project. Now, I'm onto the documentation which will take 2 more days. No significant challenges yet.",
            # ... add more name-context pairs as needed
        }

        results = identifyTasks(names_and_contexts)
        print('results::::::::::::::',results)
        data=dict(request.POST)
        no_person = len([i for i in dict(request.POST).keys() if 'name' in i])
        persons = [i for i in dict(request.POST).keys() if 'name' in i]
        persons = [data[person][0] for person in persons]
        tasks = [i for i in dict(request.POST).keys() if 'task' in i]
        tasks = [data[task][0] for task in tasks]
        details = []
        print(persons, tasks)

        for counter in range(0,no_person):
            details.append({'name':persons[counter],"email": "sahil@fakemail.com","task":tasks[counter], "Emp_num": '001',
             'Postion': 'Web Developer', 'Department': 'Web Development'})

        # import code
        # code.interact(local=dict(globals(), **locals()))
        results = identifyTasks(names_and_contexts)
        print('results::::::::::::::', results)

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

