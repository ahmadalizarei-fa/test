from django.shortcuts import render
from django.http import HttpResponse

import requests


res = requests.get('http://www.york.ac.uk/teaching/cws/wws/webpage1.html')
#if res.status_code == 200: # check that the request went through
  # print the entire html, should maintain internal newlines so that when it print to screen it isn't on a single line
def index(request):
 return ( res.content)
#def index(request):
   
  # return render(request, "index.html")

