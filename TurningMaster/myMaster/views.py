from django.shortcuts import render,redirect
from .forms import Registration,Enter
def main(request):
    return render(request,'main.html',)
def mainRedirect(request):
    return render(request,'main.html',)
def reg(request):
    registration = Registration()
    return render(request,'reg.html', {"form":registration})
def enter(request):
    return render(request,'enter.html',{"form":Enter})
def catalog(request):
    return render(request,'catalog.html',)
def info(request):
    return render(request,'info.html',)
def process(request):
    return render(request,'process.html',)
def machine(request):
    return render(request,'machine.html',)
def guide(request):
    return render(request,'guide.html',)

def isValidForms(request):
    if request.method == "POST":
        registration = Registration(request.POST)
        if registration.is_valid():
            return render(request, "main.html")
        else:
            return render(request, "reg.html", {'form': Registration})
def politics(request):
    return render(request,'politics.html',)