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
    def get(self,request):


        details = [
            {"name": "Sahil","email":"sahil@fakemail.com","task": "Write email series","Emp_num":'001','Postion':'Web Developer','Department':'Web Development'},
            {"name": "Krishna","email":"krishna@fakemail.com", "task": "Build Free trial Form","Emp_num":'021','Postion':'Data Analyst','Department':'Data Science'},
            {"name": "Ritesh","email":"ritesh@fakemail.com","task": "Write monthly Newsletter","Emp_num":'031','Postion':'Project Manager','Department':'Overall head'},
            {"name": "Rishit","email":"rishit@fakemail.com", "task": "Work on Home page","Emp_num":'031','Postion':'NLP Developer','Department':'AI and Data Science'},
            {"name": "Saramsa","email":"sam@fakemail.com", "task": "make the layout responsive","Emp_num":'002','Postion':'Back end Web Developer','Department':'Web Development'},
        ]

        return render(request,'dashboard/display_output.html',{'data':details})

    def post(self,request):
        print('table-view:', request.POST)
        details = [
            {"name": "Sahil","email":"sahil@fakemail.com","task": "Write email series","Emp_num":'001','Postion':'Web Developer','Department':'Web Development'},
            {"name": "Krishna","email":"krishna@fakemail.com", "task": "Build Free trial Form","Emp_num":'021','Postion':'Data Analyst','Department':'Data Science'},
            {"name": "Ritesh","email":"ritesh@fakemail.com","task": "Write monthly Newsletter","Emp_num":'031','Postion':'Project Manager','Department':'Overall head'},
            {"name": "Rishit","email":"rishit@fakemail.com", "task": "Work on Home page","Emp_num":'031','Postion':'NLP Developer','Department':'AI and Data Science'},
            {"name": "Saramsa","email":"sam@fakemail.com", "task": "make the layout responsive","Emp_num":'002','Postion':'Back end Web Developer','Department':'Web Development'},
        ]

        return render(request,'dashboard/display_output.html',{'data':details})

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