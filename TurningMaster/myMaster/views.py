from django.shortcuts import render,redirect
from .forms import Registration,Enter
from myMaster.services.registrService import CreateUser as CreateUsersAll
from myMaster.services.contentServices import GetAllText
from myMaster.models import textPage

def main(request):
    return render(request,'main.html',)
def mainRedirect(request):
    return render(request,'main.html',)
def reg(request):                                      #переход на страницу формы регистрации
    message = ""
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        birthday = request.POST.get('birthday')
        reg_form = Registration(request.POST)
        if reg_form.password1 == reg_form.password2:
            password = request.POST.get('password')
            CreateUsersAll(nickname, birthday, password)
            message = "Пользователь создан"
        else:
            message = "Пароль не совпадает"
    registration = Registration()
    return render(request,'reg.html', {"form":registration,"message":message})
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


# def isValidForms(request):
#     if request.method == "POST":
#         registration = Registration(request.POST)
#         if registration.is_valid():
#             return render(request, "main.html")
#         else:
#             return render(request, "reg.html", {'form': Registration})
def politics(request):
    return render(request,'politics.html',)

# def CreateUser(request):
#     if request.method == 'POST':
#         nickname = request.POST.get('nickname')
#         birthday = request.POST.get('birthday')
#         if Registration.password1 == Registration.password2:
#             password = request.POST.get('password')
#         else:
#             print("Пароль не совпадает")
#         GetUsersAll(nickname,birthday,password)
#     return render(request,'CreateUser.html',)


def GetAllImg(request):
    img = GetAllText()
    return render(request,'catalog.html',{'img':img})

