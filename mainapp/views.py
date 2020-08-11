from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Submit,Classes


# Create your views here.
def home(request):
    return render(request,'home.html')


def newClass(request):
	if request.method == 'POST':
		user = request.user
		name = user.username
		clsCode = request.POST['clsCode']
		cls_name = request.POST['cls_name']
		if user.is_authenticated :
			if Classes.objects.filter(clsCode=clsCode).exists():
				messages.info(request,'Security code already taken, try different one')
				return redirect('newClass')
			if Classes.objects.filter(cls_name=cls_name).exists():
				messages.info(request,'Use unique class number or class name')
				return redirect('newClass')
			else:
				x = Classes(clsCode=clsCode, cls_name=cls_name,ownedby=name)
				x.save()
				messages.info(request,'Classes is created, share the security code '+ x.clsCode+' with students now!')
				return redirect('teacherPage')
	else:
		return render(request,'newClass.html')



def studentPage(request):
	if request.method == 'POST':
		clsCode = request.POST['clsCode']
		stu_id = request.POST['stu_id']
		xs = Classes.objects.filter(clsCode__contains=clsCode)
		c=xs.count()
		if c > 0:
			obj = Submit(clsCode=clsCode,stu_id=stu_id)
			obj.save()
			messages.info(request,'Attendance Submitted')
			return redirect('studentPage')
		else:
			messages.info(request,'Invalid Class Code')
			return redirect('studentPage')
	else:
		return render(request,'studentPage.html')


def login(request):
	if request.method== 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user= auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('teacherPage')
		else:
			messages.info(request,'Wrong Password or User name!')
			return redirect('login')

	else:
		u =request.user
		if u.is_authenticated:
			return redirect('teacherPage')
		else:
			return render(request,'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')


def register(request):
	if request.method == 'POST' :
		first_name=request.POST['fname']
		last_name=request.POST['lname']
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']

		if password1==password2 :
			if User.objects.filter(username=username).exists():
				messages.info(request,'User Name Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email Taken')
				return redirect('register')
			else:	
			    user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
			    user.save();
			    return redirect('login')
		else:
		 	messages.info(request,'Password did not match')
		 	return redirect('register')
		return redirect('/')
	else:
		return render(request,"register.html")

def classList(request):
    user = request.user
    name = user.username
    if user.is_authenticated :
        x = Classes.objects.filter(ownedby=name)
        return render(request,"classList.html",{"classes":x})
    else:
        return redirect('login')


def teacherPage(request):
	user = request.user
	if user.is_authenticated:
		return render(request,'teacherPage.html')
	else:
		return redirect('login')


def classrecord(request,classname):
	user = request.user
	if user.is_authenticated:
		x = Classes.objects.filter(cls_name=classname)
		y = x[0].clsCode
		z = Submit.objects.filter(clsCode=y)
		return render(request,"show.html",{"student":z})
	else:
		return redirect('login')

