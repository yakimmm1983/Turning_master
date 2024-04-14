
from myMaster.models import regUser

def GetAllUsers():
    return regUser.objects.all()
def SaveUser(name,data,password):
    user = regUser()
    user.nickname = name
    user.birthday = data
    user.password = password
    user.save()

def CreateUser(nickname,data,password):
    try:
        regUser.nickname.get(nickname=nickname)
    except:
        user = regUser()
        user.nickname = nickname
        user.birthday = data
        user.password = password
        user.save()






