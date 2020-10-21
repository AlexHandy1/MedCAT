import sys
sys.path.insert(0, "/home/ubuntu/projects/MedCAT/")

from django.shortcuts import render
from medcat.utils.helpers import doc2html
from .models import *
import os
import json
from .apps import DemoConfig


def get_html_and_json(text):
    cat = DemoConfig.cat
    doc = cat(text)

    a = json.loads(cat.get_json(text))
    for i in range(len(a['entities'])):
        ent = a['entities'][i]

        new_ent = {}
        for key in ent.keys():
            if key == 'pretty_name':
                new_ent['Pretty Name'] = ent[key]
            if key == 'start':
                new_ent['Start Index'] = ent[key]
            if key == 'end':
                new_ent['End Index'] = ent[key]
            if key == 'cui':
                new_ent['Identifier'] = ent[key]
            if key == 'type':
                new_ent['Type'] = ent[key]
            if key == 'acc':
                new_ent['Confidence Score'] = ent[key]

            new_ent['ICD-10 Code'] = "-"
            new_ent['OPCS Code'] = "-"

            if key == 'id':
                new_ent['id'] = ent[key]

        if ent['meta_anns']:
            for meta_ann in ent['meta_anns'].keys():
                new_ent[meta_ann] = ent['meta_anns'][meta_ann]['value']

        icd10 = ent['info'].get('icd10', [])
        if icd10:
            code = icd10[-1]['chapter']
            new_ent['ICD-10 Code'] = code

        opcs = ent['info'].get('opcs', [])
        if opcs:
            code = opcs[-1]['chapter']
            new_ent['OPCS Code'] = code



        a['entities'][i] = new_ent

    doc_json = json.dumps(a)


    uploaded_text = UploadedText()
    uploaded_text.text = str(text)
    uploaded_text.save()

    return doc2html(doc), doc_json


def train_annotations(request):
    context = {}
    context['doc_json'] = '{"msg": "No documents yet"}'

    if request.POST and 'text' in request.POST:
        doc_html, doc_json = get_html_and_json(request.POST['text'])

        context['doc_html'] = doc_html
        context['doc_json'] = doc_json
        context['text'] = request.POST['text']
    return render(request, 'train_annotations.html', context=context)
