from django.shortcuts import render,redirect
from .models import list
from .forms import ListForm
from django.contrib import messages


def index(request):
    
    if request.method=='POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            allitems= list.objects.all
            messages.success(request,('Item has been added')) 
            return render(request,'index.html',{'allitems':allitems})   
    else:
        allitems=list.objects.all
        return render(request,'index.html',{'allitems':allitems})