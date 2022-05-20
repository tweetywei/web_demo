from django import forms
from .models import Feedback
from .models import Course
from django.core.validators import MaxValueValidator, MinValueValidator

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

    def clean(self):
        print('cleaning')
        data = self.cleaned_data
        if data['grade'] < 0 or data['grade'] > 6:
            raise forms.ValidationError('Grade must be numbers between 0.0 to 6.0')
        elif data['ranking_level'] < 0 or data['ranking_level'] > 5:
            raise forms.ValidationError('Ranking must be numbers between 0 to 5')
        return self.cleaned_data