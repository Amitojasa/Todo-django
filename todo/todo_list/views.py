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

def delete(request,list_id):
    item=list.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Item has been deleted'))
    return redirect('index')

def cross_off(request,list_id):
    item=list.objects.get(pk=list_id)
    item.completed=True
    item.save()
    return redirect('index')


def uncross(request,list_id):
    item=list.objects.get(pk=list_id)
    item.completed=False
    item.save()
    return redirect('index')

def edit(request,list_id):
    if request.method=='POST':
        item=list.objects.get(pk=list_id)
        form=ListForm(request.POST or None,instance=item)

        if form.is_valid():
            form.save()
            messages.success(request,('Item has been edited'))
            return redirect('index')
    else:
        item=list.objects.get(pk=list_id)
        return render(request,'edit.html',{'item':item})
