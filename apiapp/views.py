from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.


def index(request):
    response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=Arrabiata").json() 
    return render(request,'index.html',{'response':response})   