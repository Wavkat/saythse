from django import forms
from .models import Training, Contact

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = [
            'name',
            'Job',
            'Safety',
            'Supervisor',
            'JSA',
            'Risk',
            'Loading',
            'Emergency',
            'Incident',
            'LOTO',
            'Safety1',
            'Hazard',
            'Fire',
            'Electrical',
            'HotWork',
            'CHMP',
            'Ground',
            'Confined',
            'Fall',
            'Defensive',
            'Scaffold',
            'Flagman',
            'Auto',
            'Certificate',
            'Crane',
            'Rigger',
            'Hoisting',
            'Welder',
            'Diesel',
            'PPE',
            'DrLicense',
            'Qualific',
            'Heat',
            'Load',
            'GoldenRules',
            'HAVS',
            'Dropped',
            'LOF',
            'med',
        ]

