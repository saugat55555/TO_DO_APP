from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def base(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
          
            lists = List.objects.all()
            messages.success(request, 'you just add an item.')
            return render(request, 'base.html', {'lists':lists})

    else:
        lists = List.objects.all()
        return render(request, 'base.html', {'lists':lists})

def delete(request, list_id):
    itemss = List.objects.get(pk= list_id)
    itemss.delete()
    return redirect('index')

def cross_off(request, list_id):
    itemss = List.objects.get(pk= list_id)
    itemss.completed = True
    itemss.save()
    return redirect('index')

def uncross_off(request, list_id):
    itemss = List.objects.get(pk= list_id)
    itemss.completed = False
    itemss.save()
    return redirect('index')