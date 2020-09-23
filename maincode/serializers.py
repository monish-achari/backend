from rest_framework import serializers
from django.contrib.auth.models import User
import re

class SignUpSerializer(serializers.Serializer):
	"""
		serializer for the user signup form validation
	"""
	phone = serializers.CharField(max_length=100,required=True)
	password1 =serializers.CharField(max_length=100,required=True ,min_length=8)
	password =serializers.CharField(max_length=100,required=True ,min_length=8)

	def validate_phone(self,value):
		if User.objects.filter(username=value).exists():
			raise serializers.ValidationError("This Number already Exists please login")
		if not re.match(r"^\+?[0-9]{3}-?[0-9]{6,12}$",str(value)):
			raise serializers.ValidationError("Please Enter Correct Phone number for example +910123456789")
		
		return value


	def validate_password1(self,value):
		password1 = self.initial_data.get('password1')
		password2 = self.initial_data.get("password")
		if password1 and password2 and password1 != password2:
			raise serializers.ValidationError("Please Enter same password")

		if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",password2):
			raise serializers.ValidationError("Please Enter Password containing at Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character")
