from django.shortcuts import render
from django.http import HttpResponse
import io
import requests
import matplotlib.pyplot as plt
  # print the entire html, should maintain internal newlines so that when it print to screen it isn't on a single line
def index(request):
 
 res = requests.get('http://virgool.io')
 if res.status_code == 200: # check that the request went through
   return HttpResponse( res.content)


 
  
#def index(request):
   
  # return render(request, "index.html")

