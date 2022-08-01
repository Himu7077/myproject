from django.shortcuts import render,HttpResponse,redirect
from .models import signupform,userform
from .forms import signup, userformdata
from django.contrib.auth import logout
from django.core.mail import send_mail
from myproject import settings
# Create your views here.

def usersignup(request):
    myform=signup(request.POST)
    if myform.is_valid():
        myform.save()
        print('signup successfully')
        #emailsending
        subject="success"
        msg=" Hello User \nyour accout has been created with us!\n enjoy our services.\n thankyou !"
        from_id=settings.EMAIL_HOST_USER      
        to_id=['himalaygoswami43@gmail.com']
        send_mail(subject,msg,from_id,to_id)
        return redirect('home')
    else:
        print(myform.errors)

def userlogin(request):
    unm=request.POST['email']
    pas=request.POST['password']
    userid=signupform.objects.get(email=unm)
    print("userid is:",userid.id)
    user=signupform.objects.filter(email=unm,password=pas) 
    if user:
        print("login successfully")
        request.session['user']=unm
        request.session['userid']=userid.id
        return redirect('home')
    else:
        print("login faild")

def index(request):
    user=request.session.get('user')
    if request.method=="POST":
        if request.POST.get('signup')=='signup': 
            usersignup(request)           
        elif request.POST.get('login')=='login':
            userlogin(request)
            return redirect('home')
    return render(request,'index.html',{'user':user})


def contact(request):
    user=request.session.get('user')
    if request.method=="POST":
        if request.POST.get('signup')=='signup': 
            usersignup(request)           
        elif request.POST.get('login')=='login':
            userlogin(request)
            return redirect('contact')
    return render(request,'contact.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')

def updateprofile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    if request.method=='POST':
        signupfrm=signup(request.POST)
        id=signupform.objects.get(id=userid)
        if signupfrm.is_valid():
            signupfrm=signup(request.POST,instance=id)
            signupfrm.save()
            print("your profile has been updated!")
            return redirect('home')
        else:
            print(signupfrm.errors)
    return render(request,'updateprofile.html',{'user':user,'userid':signupform.objects.get(id=userid)})

def home(request):
    user=request.session.get('user')
    if request.method=="POST":
        if request.POST.get('signup')=='signup': 
            usersignup(request)           
        elif request.POST.get('login')=='login':
            userlogin(request)
            return redirect('home')
    if request.method=='POST': 
        userfrm=userformdata(request.POST,request.FILES)
        if userfrm.is_valid():
            userfrm.save()
            print("your query has been uploaded..!")
            return redirect('home')
        else:
            print(userfrm.errors)
    return render(request,'home.html',{'user':user})

def about(request):
    user=request.session.get('user')
    if request.method=="POST":
        if request.POST.get('signup')=='signup': 
            usersignup(request)           
        elif request.POST.get('login')=='login':
            userlogin(request)
            return redirect('about')
    return render(request,'about.html',{'user':user})

