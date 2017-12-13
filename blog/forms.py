from django import forms

class FormArticle(forms.Form):
	title = forms.CharField()
	publication_date = forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
	text = forms.CharField(widget=forms.Textarea)
	thumbnail = forms.ImageField()