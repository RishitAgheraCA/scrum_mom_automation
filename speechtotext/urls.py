from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic.base import RedirectView
from speechtotext.views import SpeechToTextView

urlpatterns = [
                  path('speechtotext/', SpeechToTextView.as_view(), name='speech-to-text'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
