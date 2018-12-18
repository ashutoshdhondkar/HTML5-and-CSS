from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def basic(request):
	return render(request,'index.html')

def index(request):
	if(request.method == 'POST'):
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		print("hello")
		print(name,email,password)


	return render(request,'index.html')