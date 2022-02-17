from django.shortcuts import render
from django.http import HttpResponse
import io
import requests
import matplotlib.pyplot as plt
import tensorflow as tf
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



# return response 

 mnist=tf.keras.datasets.mnist
 (x_train,y_train),(x_test,y_test)=mnist.load_data()
 response = HttpResponse(content_type="image/png")
# create your image as usual, e.g. pylab.plot(...)
 #plt.imshow(x_train[0])
 plt.savefig(response, format="png")
 return HttpResponse( response)  
 


 #plt.show()


 
  
#def index(request):
   
  # return render(request, "index.html")
 
  
