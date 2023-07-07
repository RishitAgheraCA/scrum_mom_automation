from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, 'dashboard/home_page.html')

    def post(self, request):
        return render(request, 'dashboard/home_page.html')

# class TaskPageView(View):
#     def get(self, request):
#         return render(request, 'dashboard/tabulator.html')


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