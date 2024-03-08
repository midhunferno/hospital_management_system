from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import doctor,patient,appoiment
# from hospital_app.models import 
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,"contact.html")

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors_count = doctor.objects.count()
    patients_count = patient.objects.count()
    appointments_count = appoiment.objects.count()

    context = {'doctors_count': doctors_count, 'patients_count': patients_count, 'appointments_count': appointments_count}
    
    return render(request, 'index.html', context)

def login_admin(request):
    error=""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {"error":error}
    return render(request,'login.html',d)

def logout_admin(request):
    if not request.user.is_staff:
        return redirect("login")
    logout(request)
    return redirect('login')


def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doc.html',d)        
        

def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor_instance = doctor.objects.get(id=pid)
    doctor_instance.delete()
    return redirect('viewdoc')       

def add_doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        special = request.POST['special']
      
        try:
            doctor.objects.create(name=name,mobile=mobile,special=special)
            error="no"
        except:
            error="yes"
    d={'error':error}    
    return render(request,'add_doc.html',d)


def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = patient.objects.all()
    d = {'doc':doc}
    return render(request,'view_per.html',d) 

def delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient_instance = patient.objects.get(id=pid)
    patient_instance.delete()
    return redirect('viewper')  

def add_patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login') 
    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        address = request.POST['address']
      
        try:
            patient.objects.create(name=name,gender=gender,mobile=mobile,address=address)
            error="no"
        except:
            error="yes"
    d={'error':error}    
    return render(request,'add_per.html',d)   


def add_appointment(request):
    error = ""

    if not request.user.is_staff:
        return redirect('login') 

    dr1 = doctor.objects.all()
    pa1 = patient.objects.all()

    if request.method == "POST":
        doctor_name = request.POST['doctor']
        patient_name = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']

        dr = doctor.objects.filter(name=doctor_name).first()
        pa = patient.objects.filter(name=patient_name).first()

        try:
            appoiment.objects.create(doctor=dr, patient=pa, date=date, time=time)
            error = "no"
        except:
            error = "yes"

    d = {
       'doctor': dr1,
       'patient': pa1,
       'error': error
    }

    return render(request, 'add_appointment.html', d)

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = appoiment.objects.all()
    d = {'doc':doc}
    return render(request,'view_appointment.html',d) 

def delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appoiment_instance = appoiment.objects.get(id=pid)
    appoiment_instance.delete()
    return redirect('viewapin')  

