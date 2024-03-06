from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):


    peoples = [
        {'name':'abhinav Gupta', 'age':26},
        {'name':'Rohan sharma', 'age':20},
        {'name': 'Gopal','age':21}
    ]


    for people in peoples:
        print(people)



    return render(request,"home/index.html", context={'people': peoples})

def success_page(request):
    return HttpResponse("<h1>This is a sucess page</h1>")