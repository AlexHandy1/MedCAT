from django import forms


from .models import ConceptDB

class CDBModelForm(forms.ModelForm):
	class Meta:
		model = ConceptDB
		fields = {'name', 'cdb_file'}