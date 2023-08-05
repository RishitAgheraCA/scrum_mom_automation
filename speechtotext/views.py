import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
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
        print(request.FILES)
        file = request.FILES['audio_data']
        filename = request.POST.get('filename')
        print('filename', filename)

        #Number of participants on the scrum meeting
        num_users = request.POST.get('num_users')

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
        text_output = r.get_large_audio_transcription_on_silence(path, filename)
        dict = {'text': text_output}
        # with open(config.TRANSCRIPT_FILE + filename, 'r') as f:
        #     text_output = f.read()
        #     print('final text output:', text_output)
        #     dict.update({'text':text_output})
        print(dict)

        return JsonResponse({'dict':dict})

        """
        
        api call for speech recognition will come here
        
        """
        # import code
        # code.interact(local=dict(globals(), **locals()))
        # return HttpResponse(json.dumps(dict), content_type='application/json')
        person_text = [
            {"name": "Sahil", "email": "sahil@fakemail.com", "task": text_output, "Emp_num": '001',
             'Postion': 'Web Developer', 'Department': 'Web Development'},
            {"name": "Krishna", "email": "krishna@fakemail.com", "task": "Build Free trial Form", "Emp_num": '021',
             'Postion': 'Data Analyst', 'Department': 'Data Science'},
            {"name": "Ritesh", "email": "ritesh@fakemail.com", "task": "Write monthly Newsletter", "Emp_num": '031',
             'Postion': 'Project Manager', 'Department': 'Overall head'},
            {"name": "Rishit", "email": "rishit@fakemail.com", "task": "Work on Home page", "Emp_num": '031',
             'Postion': 'NLP Developer', 'Department': 'AI and Data Science'},
            {"name": "Saramsa", "email": "sam@fakemail.com", "task": "make the layout responsive", "Emp_num": '002',
             'Postion': 'Back end Web Developer', 'Department': 'Web Development'},
        ]
        return render(request, 'speechtotext/person_texts.html', {'data': person_text})


class TaskRecognition(View):
    def get(self, request):
        print(request.POST)
        return render(request, 'speechtotext/person_texts.html', {'data': person_text})

    def post(self, request):
        return render(request, 'speechtotext/person_texts.html')
