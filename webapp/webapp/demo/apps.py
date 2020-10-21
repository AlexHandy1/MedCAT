from django.apps import AppConfig
from .models import UploadedText, VocabDB, ConceptDB
from medcat.cat import CAT
from medcat.cdb import CDB
from medcat.utils.vocab import Vocab
from urllib.request import urlretrieve
import os
from django.conf import settings

#runs whenever you run manage.py - what is the best pattern for where to put this?
class DemoConfig(AppConfig):
	#copied from settings to test
	name = 'demo'

	#load cat models and make available as global variable (basic version until fix FileField issue)
	vocab_path = './data_models/vocab.dat'
	cdb_path = './data_models/cdb-medmen.dat'

	vocab = Vocab()
	vocab.load_dict(vocab_path)
	cdb = CDB()
	cdb.load_dict(cdb_path) 
	cat = CAT(cdb=cdb, vocab=vocab)

	print("cat loaded: ", cat)

	#load standard models - remote storage method (very lengthy)
	# vocab_path = os.getenv('VOCAB_PATH', "/tmp/vocab.dat")
	# cdb_path = os.getenv('CDB_PATH', "/tmp/cdb.dat")
	# vocab_url = "https://s3-eu-west-1.amazonaws.com/zkcl/vocab.dat"
	# cdb_url = "https://s3-eu-west-1.amazonaws.com/zkcl/cdb-medmen.dat"
	# urlretrieve(vocab_url, vocab_path)
	# urlretrieve(cdb_url, cdb_path)

	#save standard models to database
	# standard_vocab_model = VocabDB(name="standard", vocab_file=vocab_path)
	# standard_vocab_model.save()

	# standard_cdb_model = ConceptDB(name="standard", cdb_file=cdb_path)
	# standard_cdb_model.save()

	# print(VocabDB.objects.all())
	# print(ConceptDB.objects.all())
