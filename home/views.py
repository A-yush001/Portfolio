
from django.shortcuts import render,HttpResponse
from home.models import Contact

def home(request):
    #return HttpResponse("This is my home page")
    context={"name":"Ayush",'Specialisation':"Backend"}
    return render(request,'home.html',context)

def about(request):
    #return HttpResponse("This is my about page")
    return render(request,'about.html')

def project(request):
    #return HttpResponse("This is my projects page")
    return render(request,'projects.html')

def contact(request):
    if request.method=="POST":
       name=request.POST['name']
       email=request.POST['email']
       number=request.POST["number"]
       desc=request.POST["desc"]
       #print(name,email,number,desc)
       ins=Contact(names=name, email=email, phone=number, desc=desc)
       ins.save()
       print("The data has been saved in database")
    
    #return HttpResponse("This is my contact page")
    return render(request,'contact.html')