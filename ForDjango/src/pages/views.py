from django.shortcuts import render
from django.http import HttpResponse #this import allows us to return http response to the client
# Create your views here.
#this is the frontend module

def home_vu(request, *args, **kwargs):
    print ("requested by", request.user) #this line enables us to find out which user made which request
    return render (request, "index.html", {})


def contact_page (request, *args, **kwargs):
    print(request.user)
    return render (request, "contacts.html", {})

def about_page (request, *args, **kwargs):
    print(request.user)
    my_dict = {"my_name":"My name is Samuel", "a_number": 24324,
    "street": "Dutse markaranta"
    } #this is django template contexting
    return render(request, "about.html", {})