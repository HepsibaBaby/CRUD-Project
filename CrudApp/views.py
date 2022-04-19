from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
from CrudApp.forms import LoginForm, StudentForm
from CrudApp.models import Student


def home(request):
    return render(request, 'home.html')


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('adminhome')
            elif user.is_student:
                return redirect('studenthome')
        else:
            messages.info(request, 'invalid credentials')

    return render(request, 'login.html')


def adminhome(request):
    return render(request, 'adminhome.html')


def studenthome(request):
    return render(request, 'studenthome.html')

def studentregister(request):
    login_form = LoginForm()
    student_form = StudentForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        student_form = StudentForm(request.POST)
        if login_form.is_valid() and student_form.is_valid():
            user = login_form.save(commit=False)
            user.is_student = True
            user.save()
            s = student_form.save(commit=False)
            s.user = user
            s.save()
            messages.info(request,'student registered successful')
            return redirect('student_view')
    return render(request,'studentregister.html',{'login_form':login_form,'student_form':student_form})

def studentview(request):
    s = Student.objects.all()
    return render(request,'studentview.html',{'s':s})

