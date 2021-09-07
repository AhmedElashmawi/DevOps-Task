from django.shortcuts import render,redirect
from .models import Meetup,Emolyees,Participant
from .forms import EmployeesForm, RegistrationForm , JobsForm, empReg
from django.contrib.auth import authenticate, forms, login as auth_login
from django.contrib.auth.decorators import login_required


# from django.http import HttpResponse
# Create your views here.


def index(request):
    meetups = Meetup.objects.all() #all ==> show all data
    
    return render(request,'meetups/index.html',        
    {
        'show_meetups':True,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup =Meetup.objects.get(slug=meetup_slug)
        if request.method =='GET':
            registration_form = RegistrationForm()
            print(request.user.email)
            if request.user.is_authenticated:
                registration_form.fields['email'].initial=request.user.email
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
            
                # user_email = registration_form.cleaned_data['email']
                participant = registration_form.save()
                # participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)

                return redirect('confirm-registration',meetup_slug=meetup_slug)### erooor not direct right 
            else:
                print(False)    
        return render(request,'meetups/meetup_details.html',{
                'meetup_found':True,    
                'meetup': selected_meetup,
                'form': registration_form
            })
    except Exception as exc:
        print(exc)
        return render(request,'meetups/meetup_details.html',{
            'meetup_found': False
        })



def confirm_registration(request,meetup_slug):
    meetup =Meetup.objects.get(slug=meetup_slug)
    return render(request,'meetups/registration-sucess.html',{
        'organizer_email' : meetup.organizer_email
    })



##### note i change meetups to account if not work just bring it back 
def login(request):
    return render(request,'accounts/login.html')


def reg(request):
    return render(request,'meetups/reg.html')



########################################################
#                                                      #
#      I use these method to crud Meetups (Jobs)       #
#                                                      #
########################################################

## This Section To handel Adding Jobs Views
def addJobs(request):
    form = JobsForm()

    if request.method == 'POST':
        form = JobsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/meetups')
    
    else:
        form=JobsForm()

    context = {
        "form":form
    }
    return render(request,'meetups/addJobs.html',context)


def updateJobs(request,pk):
    jobs = Meetup.objects.get(id=pk)
    form = JobsForm(instance=jobs)

    if request.method == 'POST':
        form = JobsForm(request.POST,request.FILES, instance=jobs)
        if form.is_valid():
            form.save()
            return redirect('/meetups')
        else:
            form=updateJobs()
    
    context = {
        "form":form
    }
    return render(request,'meetups/updateJobs.html',context)


def deleteJobs(request,pk):
    jobs = Meetup.objects.get(id=pk)
    jobs.delete()
    return redirect('/meetups')

########################################################
#                                                      #
#      I use these method to crud Employee             #
#                                                      #
########################################################

def addEmployee(request):
    # form = EmployeesForm()
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        profile_form = empReg(request.POST)


        if form.is_valid() and profile_form.is_valid():
           user = form.save()
           profile = profile_form.save(commit=False)
           profile.user = user
           profile.save()
           
           
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           user = authenticate(username=username,password=password)
           login(request)
           return redirect('/login')
    else:
        form=EmployeesForm()
        profile_form=empReg()

    context = {"form":form,'profile_form': profile_form}
    return render(request,'meetups/addEmployee.html',context)


def updateEmployee(request,pk):
    employee = Emolyees.objects.get(id=pk)
    form = EmployeesForm(instance=employee)

    if request.method == 'POST':
        form = EmployeesForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/meetups')
    context = {
        "form":form
    }
    return render(request,'meetups/updateEmployee.html',context)


def deleteEmployee(request,pk):
    employee = Emolyees.objects.get(id=pk)
    employee.delete()
    return redirect('/meetups')

    

