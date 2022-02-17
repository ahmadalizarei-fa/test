from django.shortcuts import render
from django.http import HttpResponse
import io
import requests
import matplotlib.pyplot as plt
  # print the entire html, should maintain internal newlines so that when it print to screen it isn't on a single line
def index(request):
 
 #res = requests.get('http://virgool.io')
 #if res.status_code == 200: # check that the request went through
  # return HttpResponse( res.content)

# creating plotting data
 xaxis =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 yaxis =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
# plotting 
 plt.plot(xaxis, yaxis)
 plt.xlabel("X")
 plt.ylabel("Y")
  
# saving the file.Make sure you 
# use savefig() before show().
 plt.savefig("squares.png")
 byte buf 
 plt.savefig(buf, format='png')
 plt.close(fig)

 response = HttpResponse(buf.getvalue(), content_type='image/png')

 #plt.show()

 return response

 
  
#def index(request):
   
  # return render(request, "index.html")
 
  
