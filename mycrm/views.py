from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, addRecord
from .models import NewFile
from django.http import JsonResponse
from django.shortcuts import HttpResponse

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

# views.py


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def list_files(request):
    files = NewFile.objects.values('name').distinct()
    file_list = [file['name'] for file in files]
    if is_ajax(request) and request.method == 'GET':
        files = request.GET.get('files', None)
        # Process the selected file and return appropriate data
        # Example: cities = YourModel.objects.filter(upload=files).values('name')
        # Return JsonResponse with the data
        #return JsonResponse({'files': []})  # Replace with actual data


    return render(request, 'view_records.html', {'file_list': file_list})




