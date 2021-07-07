from django.shortcuts import render

#Create your views here.

data={

'tital':['java','php','android','html'],

'list':[
    
    {'name':'saurabh','contact':7359747893}
]
}

def home(request):
    return render(request,"index.html",data)