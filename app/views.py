from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
    #if request.GET:
    #   return HttpResponse(f'GET {dict(request.GET)}') #try http://127.0.0.1:8000/app/?id=10&name=app1
    return redirect('listAllApps')

def appByName(request, name):
    return HttpResponse(f"{name} app")

def listAllApps(request):
    return HttpResponse("app1, app2, app3, ...")

def addApp(request):
    return HttpResponse("Add app here...")
