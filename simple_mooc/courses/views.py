from django.shortcuts import render

from courses.models import Course


def index(request):
    context = {}
    context['courses'] = Course.objects.all()
    return render(request, 'index.html', context)


def course(request, slug):
    context = {}
    context['courses'] = Course.objects.get(slug=slug)
    return render(request, 'course.html', context)
