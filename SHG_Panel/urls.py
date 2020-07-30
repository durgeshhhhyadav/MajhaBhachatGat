from django.urls import path
from . import views

urlpatterns = [
	path('', views.home ),
	path('dashboard/', views.Dashboard ),
	path('signup/', views.Signup ),
	path('verifyotp/', views.VerifyOTP ),
	path('login/', views.Login ),
	path('logout/', views.logout_call ),
	path('sms/', views.Sms),
]