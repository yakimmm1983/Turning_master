from myMaster.models import textPage

def GetAllText():
    return textPage.objects.all()


def SaveText(text,img):
    allText = textPage()
    allText.text = text
    allText.img = img
    allText.save()


