from django.shortcuts import render

from courses.models import Course

def index(request):
    context = {}
    context['courses']= Course.objects.all()
    return render(request, 'courses.html', context)
