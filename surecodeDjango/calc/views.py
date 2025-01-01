from django.http import HttpResponse
from django.shortcuts import render

from .models import StudentORM


# Create your views here.

def home(req):
    # This all it takes to fetch the data from Database
    studentsData = StudentORM.objects.all()
    return render(req,"home.html",{'name':'Suresh', "data":studentsData})
    # return HttpResponse("Hello world")
def add(req):
    val1 = int(req.POST['num1'])
    val2 = int(req.POST['num2'])
    # If it is present in url we can use GET
    # val1 = int(req.GET['num1'])
    # val2 = int(req.GET['num2'])
    val3 = val1 + val2
    return render(req,"result.html",{'result':val3})
    # return HttpResponse("Hello world")