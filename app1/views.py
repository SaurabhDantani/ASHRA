from django.shortcuts import render

#Create your views here.

from django.http import HttpResponse

def header(request):
	return render(request,'header.html')

def index(request):
    	return render(request,'index.html')

def footer(request):
    	return render(request,'footer.html')

def contact(request):
    	return render(request,'contact.html')

def why(request):
    	return render(request,'why-us.html')

def client(request):
    	return render(request,'client.html')

def client(request):
	return render(request,'client.html')

def skills(request):
    	return render(request,'skills.html')