from django import forms
from .models import Feedback
from .models import Course

class FeedbackForm(forms.ModelForm):
    # course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Feedback
        fields = "__all__"
    '''
        widgets = {
            'student_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'grade' : forms.NumberInput(attrs={'class': 'form-control'}),
            'ranking_level' : forms.NumberInput(attrs={'class': 'form-control'}),
        }
    '''