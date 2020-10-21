from django.db import models

# Create your models here.
class UploadedText(models.Model):
    text = models.TextField(default="", blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

class ConceptDB(models.Model):
	name = models.CharField(max_length=100, default='', blank=True)
	cdb_file = models.FileField(upload_to='data_models')

class VocabDB(models.Model):
	name = models.CharField(max_length=100, default='', blank=True)
	vocab_file = models.FileField(upload_to='data_models') 