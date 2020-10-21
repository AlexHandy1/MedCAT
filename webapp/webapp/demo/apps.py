from django.apps import AppConfig
from medcat.cat import CAT
from medcat.cdb import CDB
from medcat.utils.vocab import Vocab
from urllib.request import urlretrieve
import os

class DemoConfig(AppConfig):
    name = 'demo'
    vocab_path = os.getenv('VOCAB_PATH', "/tmp/vocab.dat")
    cdb_path = os.getenv('CDB_PATH', "/tmp/cdb.dat")
    vocab_url = "https://s3-eu-west-1.amazonaws.com/zkcl/vocab.dat"
    cdb_url = "https://s3-eu-west-1.amazonaws.com/zkcl/cdb-medmen.dat"

    #why don't these physical get added to models folder?
    urlretrieve(vocab_url, vocab_path)
    urlretrieve(cdb_url, cdb_path)

    vocab = Vocab()
    vocab.load_dict(vocab_path)
    print("Vocab", vocab)
    
    cdb = CDB()
    cdb.load_dict(cdb_path)
   
    print("CDB", cdb)
    
    cat = CAT(cdb=cdb, vocab=vocab)
    print("CAT", cat)
    cat.spacy_cat.MIN_ACC = 0.30
    cat.spacy_cat.MIN_ACC_TH = 0.30
    cat.spacy_cat.ACC_ALWAYS = True
