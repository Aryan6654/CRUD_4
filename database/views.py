from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import EmployeeRegistrations
from django.forms import forms
from django.contrib import messages

# Create your views here.
def add_user(request):
    if request.method == 'POST':
        fm = EmployeeRegistrations(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ad = fm.cleaned_data['address']
            reg = User(name=nm, email=em, address=ad)
            reg.save()
            messages.success(request, nm)
            fm = EmployeeRegistrations()
    else:
        fm = EmployeeRegistrations()
    show = User.objects.all()

    return render(request, 'addandshow.html', {'form':fm, 'sho':show})

#This function will Update
def update_data(request, id):
    if request.method == 'POST':
        ef = User.objects.get(pk=id)
        fm = EmployeeRegistrations(request.POST, instance=ef)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            fm.save()
            messages.success(request, nm)
    else:
        ef = User.objects.get(pk=id)
        fm = EmployeeRegistrations(instance=ef)
    return render(request, 'updateandedit.html', {'form':fm})

#This function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        ef = User.objects.get(pk=id)
        ef.delete()
        return HttpResponseRedirect('/')