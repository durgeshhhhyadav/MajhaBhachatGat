from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import *

from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from . sms_varification import SmsVarification

# Create your views here.
OTP = 0
mob = 0


def home(request):
	return render(request, 'index.html')

@login_required
def Dashboard(request):
	print(request.user.id)
	return render(request, 'base.html')

def Signup(request):
	global OTP, mob
	if request.method == 'POST':
		mobileNumber = request.POST['mobile_number']
		email = request.POST['email']
		firstName = request.POST['first_name']
		middleName = request.POST['middle_name']
		lastName = request.POST['last_name']
		inputPassword = request.POST['password']
		confirmPassword = request.POST['confirm_password']

		if inputPassword == confirmPassword:

			user = User(first_name=firstName, 
						last_name=lastName, 
						username=mobileNumber, 
						email=email)
			user.set_password(inputPassword)


			message_sid,OTP = SmsVarification(mobileNumber)
			mob = mobileNumber
			

			print('views'+str(message_sid)+str(OTP))
			if message_sid:
				user.save()
				userprofile = UserProfile(Middle_Name = middleName)
				userprofile.user = user
				userprofile.save()

				return redirect('/verifyotp/')
			else:
				return redirect('/signup/')
		else:
			url = '/signup/'

			return HttpResponse('<script>alert("Your Password and Confirm Password did not match...");\
             window.location="%s"</script>'%url)
	else:
		return render(request, 'register.html')

def VerifyOTP(request):
	global OTP, mob
	if request.method == 'POST':

		otp_input = request.POST['otp']
		print(type(otp_input))
		print(OTP)
		print(type(OTP))

		if int(OTP) == int(otp_input):
			user_profile = UserProfile.objects.filter(user__username = mob)
			print("hello",user_profile)
			user_profile.update(verification = True)
			return redirect('/dashboard/')
		else:
			url = '/login/'

			return HttpResponse('<script>alert("Your OTP is not varify...");\
             window.location="%s"</script>'%url)
	else:
		
		return render(request, 'verify-otp.html')


def Login(request):
	global OTP,mob
	if request.method == 'POST':
		username = request.POST['mobile_number']
		password = request.POST['password']

		userSelected = authenticate(username=username, password=password)
		print(userSelected)
		if userSelected:	
			
			userData = UserProfile.objects.get(user = userSelected.id)

			print('udata ',userData.verification)
			if userData.verification == True :
				login(request, userSelected)
				return redirect('/dashboard/')
			else:
				message_sid,OTP = SmsVarification(userSelected.username)
				mob = userSelected.username
				return redirect('/verifyotp/')

		else:
			return HttpResponse('<h1>you have entered wrong credentials or you are not activated. Login again <a href="/login/">Click here</a>...</h1>')
	else:
			return render(request, 'login.html')

@login_required
def logout_call(request):
	logout(request)
	return redirect('/login/')

def Sms(request):
	pass
	return render(request, 'register.html')