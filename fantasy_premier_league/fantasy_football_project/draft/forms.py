from django import forms
from .models import League, Team


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class LeagueForm(forms.ModelForm):
    # draft_date = forms.DateTimeField()
    class Meta:
        model = League
        fields = ["league_name", "max_teams","draft_date"]
        widgets = {
            "draft_date": DateTimeInput(),
        }

class JoinLeagueForm(forms.ModelForm):
    # draft_date = forms.DateTimeField()
    league = forms.CharField()
    class Meta:
        model = Team
        fields = ["team_name", "league"]