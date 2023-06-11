from django.shortcuts import render,redirect
from .models import blogModel,commentModel
from blog_app.forms import blogAppCreateForm

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



def comment(request):
    form = blogAppCreateForm()
    context={"form":form}
    if request.method =="POST":
        obj = blogAppCreateForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('index_post')
        return redirect('index_post')
    return render(request,"blogs/show.html",context)