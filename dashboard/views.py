from django.shortcuts import render
from django.views import View


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, 'dashboard/home_page.html')

    def post(self, request):
        return render(request, 'dashboard/home_page.html')



class SubmitView(View):
    def get(self, request):
        return render(request, 'dashboard/home_page.html')

    def post(self, request):
        print(self.request.POST)
        import code
        code.interact(local=dict(globals(), **locals()))
        return render(request, 'dashboard/home_page.html')
