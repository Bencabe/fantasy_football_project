from django import forms
from .models import League
# import floppyforms as forms


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class LeagueForm(forms.ModelForm):
    # draft_date = forms.DateTimeField()
    class Meta:
        model = League
        fields = ["name", "max_teams","draft_date"]
        widgets = {
            "draft_date": DateTimeInput(),
        }