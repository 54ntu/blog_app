from django.shortcuts import render
from .models import blogModel

# Create your views here.
def index(request):
    blogs=blogModel.objects.all()
    context={
        'blogs':blogs
        }
    return render(request,'blogs/index.html',context)


def show(request,id):
    posts=blogModel.objects.get(id=id)
    context={
        'posts':posts
    }
    return render(request,'blogs/show.html',context)


def about(request):
    return render(request,'blogs/about.html')

def contact_post(request):
    return render(request,'blogs/contact.html')