from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from feedback_form.models import Feedback

# Create your views here.
def dashboard(request):
    feedback_data = Feedback.objects.all().values()
    template = loader.get_template('dashboard.html')
    ranking = [0] * 6
    grade = [0] * 7

    for record in feedback_data:
        ranking[record['ranking_level']] += 1
        grade[int(record['grade'])] += 1

    context = {
        'ranking': ranking,
        'grade' : grade,
        'feedback': feedback_data
    }
    return HttpResponse(template.render(context, request))