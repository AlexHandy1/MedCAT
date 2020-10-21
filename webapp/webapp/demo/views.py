import sys
sys.path.insert(0, "/home/ubuntu/projects/MedCAT/")
from django.shortcuts import render, redirect
from medcat.utils.helpers import doc2html
from .models import UploadedText, VocabDB, ConceptDB
import os
import json
from .apps import DemoConfig
from medcat.cat import CAT
from medcat.cdb import CDB
from medcat.utils.vocab import Vocab
from django.conf import settings
from .forms import CDBModelForm


def get_html_and_json(text, cat):
    #cat = DemoConfig.cat
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
    cat = DemoConfig.cat

    #load selected models from database
    # vocab = Vocab()
    # standard_vocab_model = VocabDB.objects.filter(name="standard").first()
    # vocab_path = settings.BASE_DIR + standard_vocab_model.vocab_file.path
    # print("Vocab path", vocab_path)
    # vocab.load_dict(vocab_path)
    # print("Vocab", vocab)
    
    # cdb = CDB()
    # standard_cdb_model = ConceptDB.objects.filter(name="standard").first()
    # cdb_path = settings.BASE_DIR + standard_cdb_model.cdb_file.path
    # print("CDB path", cdb_path)
    # cdb.load_dict(cdb_path)
    # print("CDB", cdb)
    
    # cat = CAT(cdb=cdb, vocab=vocab)
    # print("CAT", cat)
    
    # cat.spacy_cat.MIN_ACC = 0.30
    # cat.spacy_cat.MIN_ACC_TH = 0.30
    # cat.spacy_cat.ACC_ALWAYS = True

    if request.POST and 'text' in request.POST:
        doc_html, doc_json = get_html_and_json(request.POST['text'], cat)

        context['doc_html'] = doc_html
        context['doc_json'] = doc_json
        context['text'] = request.POST['text']
    return render(request, 'train_annotations.html', context=context)


#possible to combine?
def upload_cdb(request):
    if request.method == "POST":
        form = CDBModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('train_annotations')
    else:
        form = CDBModelForm()

    return render(request, 'upload_cdb.html', {
        'form':form
        })










