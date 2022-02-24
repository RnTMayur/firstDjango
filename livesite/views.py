from itertools import count
from turtle import ht
from django.http import HttpResponse
from django.shortcuts import redirect, render
import httplib2
from matplotlib.style import context
from .models import comapny
from .forms import sampleform
# Create your views here.
def index(request):
    data=comapny.objects.all()
    return render(request,"index.html",{'data':data})

def home_view(request):
    context={}
    form= sampleform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    
    context['form']=form
    return render(request,"index.html",context)

def insert(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        country=request.POST['country']
        app=comapny.objects.create(name=name,contact=contact,country=country)
        app.save()
        return HttpResponse("data inseted successfully")
    else:
        return HttpResponse("error")

def delete(request):
    id=request.GET['id']
    comapny.objects.filter(id=id).delete()
    return HttpResponse("data deleted")

def edit(request):
    id=request.GET['id']
    data=comapny.objects.all().filter(id=id)
    return render(request,'edit.html',{'data':data})


def edited(request):
    if request.method=='POST':
        id=request.POST["id"]
        name=request.POST['name']
        contact=request.POST['contact']
        country=request.POST['country']
        comapny.objects.filter(id=id).update(name=name,contact=contact,country=country)
        return redirect('/index')
    else:
        return HttpResponse("Data not filled")
