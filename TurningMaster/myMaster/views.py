import datetime

from django.db import IntegrityError
from django.shortcuts import render,redirect
from .forms import Registration,Enter
from myMaster.services.registrService import CreateUser as CreateUsersAll,GetAllUsers,GetUserByNickName
from myMaster.services.contentServices import GetAllText
# from myMaster.models import GetAllUsers

def main(request):
    return render(request,'main.html',)
def mainRedirect(request):
    return render(request,'main.html',)
def reg(request):                                      #переход на страницу формы регистрации
    message = ""
    if request.method == 'POST':
        try:
            nickname = request.POST.get('nickName')
            birthday = request.POST.get('dateBirth')
            birthday = datetime.datetime.strptime(birthday,'%d.%m.%Y')
            #print(birthday)
            reg_form = Registration(request.POST)
            #print(reg_form)
            if request.POST.get('password1')== request.POST.get('password2'):
                password = request.POST.get('password1')
                CreateUsersAll(nickname, birthday, password)
                message = "Пользователь создан"
            else:
                message = "Пароль не совпадает"
        except IntegrityError:
            message = "Никнейм уже существует"
    registration = Registration()
    return render(request,'reg.html', {"form":registration,"message":message})

def enter(request):
    enter = Enter()
    if request.method == 'POST':
        message = ""
        try:
            user = GetUserByNickName(request.POST.get('nickName'))
        except :
            message = "Ваш никнейм не существует или введен неправильно"
            return render(request, 'enter.html', {"form": enter, 'message': message})

        if user.password == request.POST.get('password'):
            message = "Ваш пароль не существует или введен неправильно"
        else:

            message = "Проверьте ваш никнейм или зарегистрируйтесь"

        return render(request, 'enter.html', {"form": enter, 'message': message})

    return render(request,'enter.html',{"form":enter})

def catalog(request):
    img = GetAllText()
    for im in img:
        print(im.img)
    return render(request, 'catalog.html', {'img': img})
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
def bazaHTML(request):
    return render(request,'baza.html',)
def tochenieHTML(request):
    return render(request,'tochenie.html',)

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


# def GetAllImg(request):
#     img = GetAllText()
#     return render(request,'catalog.html',{'img':img})

