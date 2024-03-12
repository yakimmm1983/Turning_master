"""
URL configuration for TurningMaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myMaster.views import main,mainRedirect,reg,enter,catalog,info,process,machine,guide,politics
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main),
    path('mainGood/',mainRedirect,name='main'),
    path('reg/',reg,name='reg'),
    path('enter/',enter,name='enter'),
    path('catalog/',catalog,name='catalog'),
    path('info/',info,name='info'),
    path('process/',process,name='process'),
    path('machine/',machine,name='machine'),
    path('guide/',guide,name='guide'),
    path('politics/',politics,name='politics'),
]
