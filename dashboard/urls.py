from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic.base import RedirectView
from dashboard.views import HomePageView, SubmitView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('submit-audio', SubmitView.as_view(), name='submit-audio'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
