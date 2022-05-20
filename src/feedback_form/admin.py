from django.contrib import admin
from .models import Course, Feedback

# Register your models here.
class CourseFeedbackAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'course', 'grade', 'ranking_level']
    list_filter = ['course']
    search_fields = ['course__name']

    class Meta:
        model = Feedback

admin.site.register(Feedback, CourseFeedbackAdmin)
admin.site.register(Course)