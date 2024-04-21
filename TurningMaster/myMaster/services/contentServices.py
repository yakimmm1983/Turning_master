from myMaster.models import textPage

def GetAllText():
    return textPage.objects.all().values_list()


def SaveText(text,img):
    allText = textPage()
    allText.text = text
    allText.img = img
    allText.save()


