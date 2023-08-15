import json

from django.http import HttpResponse
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
        dicts = {'text': text_output}
        # with open(config.TRANSCRIPT_FILE + filename, 'r') as f:
        #     text_output = f.read()
        #     print('final text output:', text_output)
        #     dict.update({'text':text_output})
        print(dicts)
        """
        
        api call for speech recognition will come here
        
        """
        # import code
        # code.interact(local=dict(globals(), **locals()))
        # return HttpResponse(json.dumps(dict), content_type='application/json')

        from transformers import AutoTokenizer, AutoModelForTokenClassification
        from transformers import pipeline
        # from huggingface_hub import notebook_login
        # access_token = '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'
        tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
        model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

        nlp = pipeline("ner", model=model, tokenizer=tokenizer)
        example = """I am John. I have done Login page development. And I will deliver the signup module this Friday. I have no blocker. I am Peter. I have Model training done. And I will deliver the Model Evaluation. I am facing difficulties in Chart creation. 
I am Sara. I have done speaker diarization. And I will deliver the Task identification module in two days. I am facing challenges in deployment. 
I am Krishna. I have created the front end. And I will be delivering the detailed view table today."""

        ner_results = nlp(example)
        print(ner_results)
        persons = []
        for a in ner_results:
            if a['entity'] == 'B-PER':
                persons.append(a['word'])

        final_dict = dict(zip(persons, split(example, persons)))
        print(final_dict)
        # import code
        # code.interact(local=dict(globals(), **locals()))
        final_dict = {'John':'I have done Login page development. And I will deliver the signup module this Friday. I '
                             'have no blocker.',
                      'Peter':'I have Model training done. And I will deliver the Model '
                                                        'Evaluation. I am facing difficulties in Chart creation.',
                      'Sara':'I have done speaker diarization. And I will deliver the Task identification module in '
                             'two days. I am facing challenges in deployment.'}


        person_text = []
        for speaker,text in final_dict.items():
            person_text.append({"name": speaker, "email": "sahil@fakemail.com", "task": text, "Emp_num": '001',
             'Postion': 'Web Developer', 'Department': 'Web Development'})
        print(person_text)
        # person_text = [
        #     {"name": "Sahil", "email": "sahil@fakemail.com", "task": text_output, "Emp_num": '001',
        #      'Postion': 'Web Developer', 'Department': 'Web Development'},
        #     {"name": "Krishna", "email": "krishna@fakemail.com", "task": "Build Free trial Form", "Emp_num": '021',
        #      'Postion': 'Data Analyst', 'Department': 'Data Science'},
        #     {"name": "Ritesh", "email": "ritesh@fakemail.com", "task": "Write monthly Newsletter", "Emp_num": '031',
        #      'Postion': 'Project Manager', 'Department': 'Overall head'},
        #     {"name": "Rishit", "email": "rishit@fakemail.com", "task": "Work on Home page", "Emp_num": '031',
        #      'Postion': 'NLP Developer', 'Department': 'AI and Data Science'},
        #     {"name": "Saramsa", "email": "sam@fakemail.com", "task": "make the layout responsive", "Emp_num": '002',
        #      'Postion': 'Back end Web Developer', 'Department': 'Web Development'},
        # ]
        return render(request, 'speechtotext/person_texts.html', {'data': person_text,})

def split(txt, seps):
    default_sep = seps[0]

    # we skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]

class TaskRecognition(View):
    def get(self, request):
        print(request.POST)
        return render(request, 'speechtotext/person_texts.html', {'data': person_text})

    def post(self, request):
        return render(request, 'speechtotext/person_texts.html')
