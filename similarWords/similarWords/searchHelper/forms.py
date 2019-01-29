from django import forms

class wordSelectForm(forms.Form):
    similarWords = forms.ChoiceField(
        widget=forms.RadioSelect
    )

    def __init__(self, word_choices=None, *args, **kwargs):
        super(wordSelectForm, self).__init__(*args, **kwargs)
        if word_choices:
            self.fields['similarWords'].choices = word_choices