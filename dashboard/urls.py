from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic.base import RedirectView
from dashboard.views import HomePageView
from dashboard.views import TaskPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('task',TaskPageView.as_view(),name='task')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
