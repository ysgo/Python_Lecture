# Create your views here.
from django.shortcuts import render, HttpResponse
import random

def index(request):
    #return HttpResponse('Welcome to Django')
    return render(request, 'index.html')

def hola(request):
    #return HttpResponse('Hello, my name is go')
    return render(request, 'hola.html')

def dinner(request):
    menus = ['피자', '치킨', '족발', '라면']
    ## random.choice는 random 중 1개 추출 할 때 사용
    ## random.sample는 여러개 추출 할 때 사용
    dinner = random.choice(menus)
    # return HttpResponse(f'오늘의 저녁 메뉴는 {dinner}입니다.')
    return render(request, 'dinner.html', {'menus':menus, 'dinner':dinner})

def lotto(request):
    numbers = range(1, 46)
    my_lotto = random.sample(numbers, 6)
    return HttpResponse(f'오늘의 로또 추천번호는 {my_lotto}입니다.')

# Variable Routing

def hello(request, name):
    return render(request, 'hello.html', {'name':name})

def introduce(request, name, age):
    return render(request, 'introduce.html', {'name':name, 'age':int(age)})

def square(request, x, y):
    result = x * y
    return render(request, 'square.html', {'x':x, 'y':y, 'result':result})