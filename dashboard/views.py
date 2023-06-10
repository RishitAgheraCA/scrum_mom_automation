from django.shortcuts import render
from django.views import View


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, 'dashboard/home_page.html')

    def post(self, request):
        return render(request, 'dashboard/home_page.html')

class TaskPageView(View):
    def get(self, request):
        return render(request, 'dashboard/tabulator.html')