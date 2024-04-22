from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.
def core_home(request):
    return render(request,'core/index.html')


def core_contact(request):
    return render(request,'core/contact.html')


def core_about(request):
    return render(request,'core/about.html')

def core_gallery(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request,'core/gallery.html',context=context)
