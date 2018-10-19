from django.shortcuts import render, HttpResponse, redirect
from apps.course.models import Course, Description
from django.contrib import messages

def index(request):
    context = {
        "course": Course.objects.all(),
        "description": Description.objects.all()
    }
    print(context)
    return render(request, "course/index.html", context)

def destroy(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request,"course/destroy.html", context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')

def process(request):
    errors = Course.objects.validation(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request,value,extra_tags=key)
        return redirect ('/')
    else:
        Course.objects.create(name = request.POST['name'])
        course = Course.objects.last()
        Description.objects.create(description = request.POST['description'],course=course)
        messages.success(request,"Course successfully created")
        return redirect('/')
