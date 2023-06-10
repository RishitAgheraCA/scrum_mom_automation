import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .services.transcriber import Transcriber
from CONFIG import config


class SpeechToTextView(View):
    def get(self, request):
        return render(request, 'dashboard/temp.html')

    def post(self, request):
        print('got it')
        from django.core.files.storage import default_storage
        from django.core.files.base import ContentFile
        file = request.FILES['audio_data']
        filename = request.POST.get('filename')
        print('filename', filename)
        path = default_storage.save(f'speechtotext/services/recordings/{filename}', ContentFile(file.read()))
        transcriber = Transcriber()
        text = transcriber.to_text(filename)
        text_output = ''
        dict = {}
        with open(config.TRANSCRIPT_FILE + filename, 'r') as f:
            text_output = f.read()
            print('final text output:', text_output)
            dict.update({'text':text_output})
        # import code
        # code.interact(local=dict(globals(), **locals()))
        return HttpResponse(json.dumps(dict), content_type='application/json')

# Create your views here.
