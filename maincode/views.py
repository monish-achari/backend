from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignUpSerializer
from django.contrib.auth.models import User
from backend.settings import AUTH_URL
import requests

# Create your views here.

class SignUp(APIView):
	"""
	user sign up using distinct mobile number
	password

	"""
	def post(self,request):
		data = request.data
		user_serializer = SignUpSerializer(data=data)
		if user_serializer.is_valid():
			obj = User.objects.create(username=data.get('phone'))
			obj.set_password(data.get('password'))
			obj.save()
			response = {"status":2,"message":"Success","error":None}
		else:
			response = {"status":0,"message":"Failed","error":user_serializer.errors}
		return Response(response)


class Login(APIView):
	"""
	user login api 
	"""

	def post(self,request):
		# import ipdb; ipdb.set_trace()
		data = request.data
		userdata = {"username":data.get('phone'),'password':data.get('password')}
		token_url = AUTH_URL +"api/v1/user/token/"
		token = requests.post(token_url,userdata)
		if token.status_code == 200:
			response = {"status":2,"message":"success"}
			response.update(token.json())
		else:
			response = {"status":0,"message":"Failure"}
			response.update(token.json())
			
		return Response(response)





