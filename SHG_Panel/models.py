from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	Middle_Name = models.CharField(max_length=50,null = True)

	verification = models.BooleanField(default = False)
