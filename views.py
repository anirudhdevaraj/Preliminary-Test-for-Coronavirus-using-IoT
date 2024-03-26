from django.shortcuts import render, redirect
from dappx.register_form import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .data import TestingForm 
from .Form import PatientForm
from .models import Patient, Testing
from django.contrib import messages


def index(request):
    return render(request, 'dappx/index.html')

def about_page_view(request):
    return render(request, 'dappx/about.html')

def iotdata_view(request): 
    return render(request, "dappx/iotdata.html")

def iotdetails_view(request): 
    return render(request, "dappx/details.html")

@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'dappx/registration.html',
                  {'user_form': user_form,
                   'registered': registered
                   })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f"They used username: {username} and password:{password}")
            return HttpResponse("Invalid login details give")
    else:
        return render(request, 'dappx/login.html', {})



def patient_view(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PatientForm()
        messages.success(request, 'Data Stored')
    context = {
        'form': form
    }
    return render(request, "dappx/details.html", context)

def testing_view(request):
    form = TestingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TestingForm()
        #messages.success(request, 'Entry Permitted.')
        return redirect("iotdetails")
    else:
        messages.success(request, '---------Entry Permit----------')

    context = {
        'form': form
    }

    return render(request, "dappx/iotdata.html", context)

def testing_list_view(request):
    queryset = Testing.objects.all() 
    context = {
        "object_list": queryset
    }
    return render(request, "dappx/testing_list.html", context)

def testing_detail_view(request, id):
    obj = Testing.objects.get(id=id)
    context = {
        "object": obj
    }
    return render(request, "dappx/testing_detail.html", context)


def testing_delete_view(request, id):
    obj = Testing.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("testing_list")
    context = {
        "object": obj
    }
    return render(request, "dappx/testing_delete.html", context)

def testing_update_view(request, id=id):
    obj = Testing.objects.get(id=id)
    form = TestingForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Updated')
    context = {
        'form': form
    }
    return render(request, "dappx/testing_create.html", context)


def testing_create_view(request):
    form = TestingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TestingForm()
    context = {
        'form': form
    }
    return render(request, "dappx/testing_create.html", context)

def patient_list_view(request):
    queryset = Patient.objects.all() 
    context = {
        "object_list": queryset
    }
    return render(request, "dappx/patient_list.html", context)

def patient_detail_view(request, id):
    obj = Patient.objects.get(id=id)
    context = {
        "object": obj
        }
    return render(request, "dappx/patient_detail.html", context)

def patient_delete_view(request, id):
    obj = Patient.objects.get(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("patient_list")
    context = {
        "object": obj
    }
    return render(request, "dappx/patient_delete.html", context)

def patient_update_view(request, id=id):
    obj = Patient.objects.get(id=id)
    form = PatientForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data Updated')
    context = {
        'form': form
    }
    return render(request, "dappx/patient_create.html", context)

def patient_create_view(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PatientForm()
    context = {
        'form': form
    }
    return render(request, "dappx/patient_create.html", context)