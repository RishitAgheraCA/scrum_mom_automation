from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic.base import RedirectView
from dashboard.views import HomePageView, SubmitView, TextView
from dashboard.views import HomePageView
from dashboard.views import TaskPageView
from dashboard.views import MainPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('task',TaskPageView.as_view(),name='task'),
    path('load',TaskPageView.as_view(),name='task_load'),
    path('main',MainPageView.as_view(),name='task_main'),
    path('text',TextView.as_view(),name='text')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
