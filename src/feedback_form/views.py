from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.
def feedback_form(request):
    error = ""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'feedback_form/received_form.html')
        else:
            error = "Invalid field value detected, please fix it before submitting"

    else:
        form = FeedbackForm()
    return render(request, 'feedback_form/feedback_form.html', {'form': form, 'error': error})