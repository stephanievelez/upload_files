from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, addRecord

from django.contrib.admin import widgets


# Create your views here.
#login function
def home(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('home')
        else:
            messages.success(request, 'Invalid Credentials')
            return redirect('home')
    else:
        return render(request, 'home.html')

    return render(request, 'home.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')


def Register_user(request):
    form = SignUpForm()
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Registered')
            return redirect('home')
        else:
            messages.success(request, 'Invalid Credentials')
            return redirect('Register')
    else:
        form = SignUpForm()
        return render(request, 'Register.html', {'form':form})
    return render(request, 'Register.html')


def add_record(request):
    form = addRecord()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = addRecord(request.POST, request.FILES)
            if form.is_valid():
                #form.upload = request.FILES['file'] #forms.Forms doesn't have save() method, so you have call the object
                #handlhandle_uploaded_file(request.FILES['file'])
                # title = form.cleaned_data['title']
                # file = form.cleaned_data['file']
                form.save()
                messages.success(request, 'File added successfully')

                return redirect('view_records')
    else:

        messages.success(request, 'You must have to login to add file')
        #return redirect('home')
        form = addRecord()

    return render(request, 'add_record.html', {'form': form})

def list_files(request):
    csv_files = add_record(request)
    if csv_files:
        dropdown = widgets.Select(choices=[f.name for f in csv_files])
        return render(request, 'view_records.html', {'files': dropdown})
    else:
        return None

    return render(request, 'view_records.html')


