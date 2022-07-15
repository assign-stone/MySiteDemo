from django.shortcuts import render

# Create your views here.
def OpenHOME(request):
    return render(request,'home.html')

def LoginDetails(request):
    return render(request,'login.html')

def Form(request):
    return render(request,'form.html')