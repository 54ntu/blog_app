from django.shortcuts import render,redirect
from .models import blogModel,commentModel,messageQuery
from blog_app.forms import blogAppCreateForm
from django.contrib import messages

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
        postObj = blogModel.objects.get(id=request.POST.get('id')) # here i am fetching id from the blog post model data
        print("data : " , request.POST)
        obj = blogAppCreateForm(data=request.POST)
        if obj.is_valid():
            #obj.title = postObj # here postobj is assigned to title of the obj( of blogappcreateform)
            obj.save()
            return redirect('index_post')
        return redirect('index_post')
    return render(request,"blogs/show.html",context)
   


def userMessage(request):
    if request.method == "POST":
        obj = messageQuery()
        obj.firstName = request.POST.get('firstname')
        obj.lastName = request.POST.get('lastname')
        obj.email = request.POST.get('email')
        obj.message = request.POST.get('message')
        obj.save()
        messages.success(request,'inquiry message sent successfully')
        return redirect('index_post')
    return redirect(request,'contact.html')

