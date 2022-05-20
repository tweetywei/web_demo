from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from feedback_form.models import Feedback
from feedback_form.models import Course

# Create your views here.

def course_list(request):
    courses = Course.objects.all().values()
    template = loader.get_template('courses.html')

    context = {
        'courses': courses
    }
    return HttpResponse(template.render(context, request))

def dashboard(request, course_id):
    feedback_data = Feedback.objects.filter(course_id=course_id).values()
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