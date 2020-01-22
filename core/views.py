from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse("<h1>Alo, {} de {} anos</h1>".format(nome, idade))

def soma(request, num1, num2):
    var = num1 + num2
    return HttpResponse("<h1>A soma de {} e {} eh igual a {}</h1>".format(num1, num2, var))