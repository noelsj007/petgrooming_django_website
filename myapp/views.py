from django.shortcuts import render, redirect
from myapp.models import register,booking,feedback
from django.http import HttpResponse
from django.contrib.auth import logout
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"service.html")
def price(request):
    return render(request,"price.html")
def bookings(request):
    return render(request,"booking.html")
def contact(request):
    return render(request,"contact.html")
def logoutUser(request):
    logout(request)
    return redirect('login')

def login(request):
    if request.method=="POST":
       if "s1" in request.POST:
           a = request.POST.get("name")
           b = request.POST.get("username")
           c = request.POST.get("email")
           d = request.POST.get("phn")
           e = request.POST.get("pwd")
           re = register(Full_name=a,Username=b,Email=c,Phone_Number=d,Password=e)
           re.save()
           urec = register.objects.filter(Username=b, Password=e)
           for j in urec:
               id=j.id
               ph=j.Phone_Number
           request.session['uname']=b
           request.session['pword'] = e
           request.session['email'] = c
           request.session['id'] = id
           request.session['name'] = a
           request.session['phno'] = ph
           msg= a +" Your Registration Succeess .........press continue "
           return render(request, "msgpage.html",{"msg":msg})
       if "s2" in request.POST:
           a = request.POST.get("t1")
           b = request.POST.get("t2")
           urec= register.objects.filter(Username=a, Password=b)
           if urec.filter(Username=a, Password=b).exists():
               for j in urec:
                   n=j.Full_name
                   e=j.Email
                   id=j.id
                   ph = j.Phone_Number
                   request.session['uname'] = a
                   request.session['pword'] = b
                   request.session['email'] = e
                   request.session['id'] = id
                   request.session['name'] = n
                   request.session['phno'] = ph
               return render(request, "userpage.html")

           else:
               msg = "Sorry Invalid user name or password. Try again"
               return render(request, "msgpagehome.html",{"msg":msg})


    return render(request,"Login.html")

def show(request):
    return render(request,"msgpage.html")

def userpage(request):
    return render(request, "userpage.html")
def booking1(request):
    bt="Basic"
    amt=49
    n=request.session['name']
    e=request.session['email']
    if request.method=="POST":
        p=request.POST.get('t1')
        bd=request.POST.get('t2')
        btt=request.POST.get('t3')
        s=request.POST.get('t4')
        ba=booking(userid=request.session['id'],username=n,email=e,petname=p,petspecies=s,bkdate=bd,bktime=btt,service=bt,charge=amt)
        ba.save()
        msg = "Thank You  "+ n + " Your Booking Accepted .........press continue "
        return render(request, "msgpage.html", {"msg": msg})
    return render(request, "booking1.html",{"bt":bt,"amt":amt,"n":n,"e":e})

def booking2(request):
    bt="Standard"
    amt=99
    n=request.session['name']
    e=request.session['email']
    if request.method=="POST":
        p=request.POST.get('t1')
        bd=request.POST.get('t2')
        btt=request.POST.get('t3')
        s=request.POST.get('t4')
        ba=booking(userid=request.session['id'],username=n,email=e,petname=p,petspecies=s,bkdate=bd,bktime=btt,service=bt,charge=amt)
        ba.save()
        msg = "Thank You  "+ n + " Your Booking Accepted .........press continue "
        return render(request, "msgpage.html", {"msg": msg})
    return render(request, "booking2.html",{"bt":bt,"amt":amt,"n":n,"e":e})

def booking3(request):
    bt="Premium"
    amt=149
    n=request.session['name']
    e=request.session['email']
    if request.method=="POST":
        p=request.POST.get('t1')
        bd=request.POST.get('t2')
        btt=request.POST.get('t3')
        s=request.POST.get('t4')
        ba=booking(userid=request.session['id'],username=n,email=e,petname=p,petspecies=s,bkdate=bd,bktime=btt,service=bt,charge=amt)
        ba.save()
        msg = "Thank You  "+ n + " Your Booking Accepted .........press continue "
        return render(request, "msgpage.html", {"msg": msg})
    return render(request, "booking3.html",{"bt":bt,"amt":amt,"n":n,"e":e})

def viewbook(request):
    mrec=booking.objects.filter(userid=request.session['id'])
    return render(request,"viewbooking.html",{"mrec":mrec})

def cancelbook(request):
    mrec=booking.objects.filter(userid=request.session['id'])
    return render(request,"cancelbooking.html",{"mrec":mrec})
def removebooking(request,id):
    booking.objects.filter(id=id).delete()
    n = request.session['name']
    msg = "Sorry  " + n + " Your Booking Cancelled .........press continue "
    return render(request, "msgpage.html", {"msg": msg})

def addfeedback(request):
    n=request.session['name']
    p=request.session['phno']
    if request.method=="POST":
        f=request.POST.get('message')
        fa=feedback(uname=n,ph=p,feed=f)
        fa.save()
        msg = "Hello " + n + " Thankyou for you valuable feedback"
        return render(request, "msgpage.html", {"msg": msg})

    return render(request,"feedback.html",{"n":n,"p":p})

def changepassword(request):
    if request.method=="POST":
        oldpass = request.POST.get("t1")
        newpass = request.POST.get("t2")
        confrmpass = request.POST.get("t3")
        u = request.session['uname']
        p = request.session['pword']
        n = request.session['name']
        if p==oldpass:
            if newpass == confrmpass:
                register.objects.filter(Username=u, Password=p).update(Password=newpass)
                msg = "Hello " + n + " Your Password has Changed"
                return render(request, "msgpage.html", {"msg": msg})


            else:
                msg = "Hello " + n + " Password missmatch"
                return render(request, "msgpage.html", {"msg": msg})
        else:
            msg = "Hello " + n + " invalid password"
            return render(request, "msgpage.html", {"msg": msg})

    return render(request, "changepassword.html")
