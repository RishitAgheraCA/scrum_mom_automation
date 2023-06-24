import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .services.large_transcriber import LargeTranslate
from .services.transcriber import Transcriber
from CONFIG import config
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class SpeechToTextView(View):
    def get(self, request):
        return render(request, 'dashboard/temp.html')

    def post(self, request):
        print('got it')
        file = request.FILES['audio_data']
        filename = request.POST.get('filename')
        print('filename', filename)
        path = default_storage.save(f'speechtotext/services/recordings/{filename}', ContentFile(file.read()))

        """ short(2-3) sentences transcriber"""
        # transcriber = Transcriber()
        # text = transcriber.to_text(filename)
        # text_output = ''
        # dict = {}
        # with open(config.TRANSCRIPT_FILE + filename, 'r') as f:
        #     text_output = f.read()
        #     print('final text output:', text_output)
        #     dict.update({'text':text_output})

        """Large audio file Transcriber"""
        path = f'speechtotext/services/recordings/{filename}'
        r = LargeTranslate()
        text_output = r.get_large_audio_transcription_on_silence(path,filename)
        dict = {'text':text_output}
        # with open(config.TRANSCRIPT_FILE + filename, 'r') as f:
        #     text_output = f.read()
        #     print('final text output:', text_output)
        #     dict.update({'text':text_output})
        print(dict)

        # import code
        # code.interact(local=dict(globals(), **locals()))
        return HttpResponse(json.dumps(dict), content_type='application/json')
