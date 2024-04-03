from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib import messages
# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
             nm=fm.cleaned_data['name'] #iiuuh
             em=fm.cleaned_data['email']
             ps=fm.cleaned_data['password']
             reg=User(name=nm,email=em,password=ps)
             reg.save()
             fm=StudentRegistration()
             messages.add_message(request,messages.SUCCESS,'Your account has been created!!!')
             messages.set_level(request,messages.DEBUG)
             messages.info(request,'This is new debug')
             print(messages.get_level(request))

    else:
            fm=StudentRegistration()
    stud=User.objects.all()                
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

def update_data(request,id):
    if request.method=='POST':
          pi=User.objects.get(pk=id)
          fm=StudentRegistration(request.POST,instance=pi)
          if fm.is_valid():
               fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)     
    return render(request,'enroll/updates.html',{'form':fm})

def delete_data(request,id):
     if request.method=='POST':
          pi=User.objects.get(pk=id)
          pi.delete()
     return HttpResponseRedirect('/')    