from django.shortcuts import render
from django.http import HttpResponse, request
from .models import onlineuser
from .models import bookings


# Create your views here.
def home(request):
	return render(request, 'index.html')

def userlogindef(request):
	return render(request, 'user.html')

def signupdef(request):
	return render(request, 'signup.html')

def usignupactiondef(request):
	email=request.POST['mail']
	pwd=request.POST['pwd']
	name=request.POST['name']
	ph=request.POST['ph']
	gen=request.POST['gen']
	age=request.POST['age']

		
	d=onlineuser.objects.filter(email__exact=email).count()
	if d>0:
		return render(request, 'signup.html',{'msg':"Email Already Registered"})
	else:
		d=onlineuser(name=name,email=email,phone=ph,pwd=pwd,gender=gen,age=age)
		d.save()
		return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})

	return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})

def userloginactiondef(request):
	if request.method=='POST':
		uid=request.POST['mail']
		pwd=request.POST['pwd']
		d=onlineuser.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()
		
		if d>0:
			d=onlineuser.objects.filter(email__exact=uid)
			name=""
			for d1 in d:
				name=d1.name

			request.session['useremail']=uid
			request.session['username']=name
			return render(request, 'user_home.html',{'data': d[0]})

		else:
			return render(request, 'user.html',{'msg':"Login Fail"})

	else:
		return render(request, 'user.html')

def userhomedef(request):
	if "useremail" in request.session:
		uid=request.session["useremail"]
		d=onlineuser.objects.filter(email__exact=uid)
		return render(request, 'user_home.html',{'data': d[0]})

	else:
		return render(request, 'user.html')

def userlogoutdef(request):
	try:
		del request.session['useremail']
	except:
		pass
	return render(request, 'user.html')


def viewrooms(request):
	if "useremail" in request.session:
		uid=request.session["useremail"]
		
		return render(request, 'viewrooms.html')

	else:
		return render(request, 'user.html')
def check(request):
	if "useremail" in request.session:
		uid=request.session["useremail"]
		
		return render(request, 'viewrooms2.html')

	else:
		return render(request, 'user.html')



def bookingdef(request):
	c1=request.POST['c1']
	c2=request.POST['c2']
	no=request.POST['no']
	email=request.POST['email']
	gen=request.POST['ph']
	st=request.POST['st']

	avail=10

		
	d=bookings.objects.filter(service__exact=st).filter(date__exact=c1).count()
	print('--------------------',d)
	if (avail-d)>0:
		d=bookings(service=st,date=c1,user=email)
		d.save()
		return render(request, 'bookingpay.html')
	else:
		
		return render(request, 'viewrooms.html',{'msg':"Not Available"})

	return render(request, 'viewrooms.html',{'msg':"Not Available"})


def userhomedef2(request):
	if "useremail" in request.session:
		uid=request.session["useremail"]
		d=onlineuser.objects.filter(email__exact=uid)
		return render(request, 'user_home.html',{'data': d[0],'m':'Thank you for booking'})

	else:
		return render(request, 'user.html')

def aboutus(request):
	if "useremail" in request.session:
		
		
		return render(request, 'about.html')

	else:
		return render(request, 'user.html')

def contactus(request):
	if "useremail" in request.session:
		
		
		return render(request, 'contact.html')

	else:
		return render(request, 'user.html')

def alogin(request):
	return render(request, 'admin.html')

def adminlogindef(request):
	if request.method=='POST':
		uid=request.POST['uid']
		pwd=request.POST['pwd']
		
		if uid=='admin' and pwd=='admin':
			request.session['adminid']='admin'
			return render(request, 'admin_home.html')

		else:
			return render(request, 'admin.html',{'msg':"Login Fail"})

	else:
		return render(request, 'admin.html')

def adminhome(request):
	if "adminid" in request.session:
		
		return render(request, 'admin_home.html')

	else:
		return render(request, 'student.html')

def alogout(request):
	try:
		del request.session['adminid']
	except:
		pass
	return render(request, 'admin.html')

def aviewrooms(request):
	if "adminid" in request.session:
		uid=request.session["adminid"]
	
		query_results = bookings.objects.all()
		return render(request, 'aviewrooms.html', {'query_results':query_results})

	else:
		return render(request, 'user.html')
