from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.


def karibu(request):
    return HttpResponse("<h1>karibu to django</h1>")
def welcome (request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,"about us.html")
def services(request):
    return render(request,'services.html')
def contactus(request):
    return  render(request,"contact us.html")
def gallery(request):
    return render(request,'gallery.html')



