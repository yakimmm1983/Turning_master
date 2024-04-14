from django.shortcuts import render,redirect
from .forms import Registration,Enter
from myMaster.services.registrService import CreateUser as GetUsersAll
from myMaster.services.contentServices import SaveText
from myMaster.models import textPage

def main(request):
    return render(request,'main.html',)
def mainRedirect(request):
    return render(request,'main.html',)
def reg(request):
    registration = Registration()
    return render(request,'reg.html', {"form":registration})
def enter(request):
    enter = Enter()
    return render(request,'enter.html',{"form":enter})
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

def CreateUser(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        birthday = request.POST.get('birthday')
        if Registration.password1 == Registration.password2:
            password = request.POST.get('password')
        else:
            print("Пароль не совпадает")
        GetUsersAll(nickname,birthday,password)
    return redirect('main')

def GetAllImg(request,img,text):
    text = SaveText(text,img)
    img = textPage.objects.all(img = img.id)
    return render(request,'catalog.html',{'text':text,'img':img})

