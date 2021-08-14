from management.models import appointment
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.


def appoint(request):
    if request.method=='POST':
        ap = appointment()
        name=request.POST.get('apname')
        num=request.POST.get('apnum')
        prob=request.POST.get('approb')
        t = request.POST.get('time')
        ap.name=name
        ap.Phone_Number=num
        ap.problem=prob
        ap.appointment_Date = t
        ap.save()
        messages.success(request,"Appointment Sent Successfully")
        return render(request,"appointment.html")
    else:
        messages.warning(request, "Appointment not sent")
        return render(request,"appointment.html")



def loginpage(request) :
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid username/login')
            return redirect('login')
    context = {}
    return render(request,'login.html',context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account was created for "+user)
            return redirect('login')
        else:
            messages.warning(request,"Account was not created")
            return redirect('register')
    context = {'form':form}
    return render(request,'register.html',context)
    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     username = request.POST['user_name']
    #     password1 = request.POST['password1']
    #     password2 = request.POST['password2']
    #     email = request.POST['email']
    #     phone_number = request.POST['phone_number']
    #     address = request.POST['address']
        
    #     if password1 == password2 :
    #         if User.objects.filter(username=username).exists():
    #             messages.info(request,'User name already taken')
    #             return redirect('register')
    #         elif User.objects.filter(email=email).exists():
    #             messages.info(request,'email already taken')
    #             return redirect('register')
    #         else:
    #             user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
    #             user.save()
    #             messages.info(request,'Account created')
    #             return redirect('login')

                
    #     else:
    #         messages.info(request,'Password and confirm password should not match')
    #         return redirect('register')
    #     return redirect('/')
    # else:
    #     return render(request,'register.html')


def logoutpage(request):
    logout(request)
    return redirect('/')