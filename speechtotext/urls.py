from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic.base import RedirectView
from speechtotext.views import SpeechToTextView, TaskRecognition

urlpatterns = [
          path('task-recognition',TaskRecognition.as_view(),name='task-recognition'),
          path('speechtotext/', SpeechToTextView.as_view(), name='speech-to-text'),
          path('upload/', SpeechToTextView.file_upload, name='upload_file'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
