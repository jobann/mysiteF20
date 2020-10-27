# Import necessary classes
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Topic, Course, Student, Order


# Create your views here.
def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index0.html', {'top_list': top_list})


def about(request):
    return render(request, 'myapp/about0.html')


def detail(request, topic_id):
    topic_name = get_object_or_404(Topic, id=topic_id).name
    topic_length = get_object_or_404(Topic, id=topic_id).length
    courses = Course.objects.filter(topic_id=topic_id)
    return render(request, 'myapp/detail0.html', {'topic_name': topic_name, 'topic_length': topic_length,
                                                  'courses': list(courses)})




