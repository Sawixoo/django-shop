from django.shortcuts import render

# Create your views here.

def index(reqest):
    return render(reqest, "index.html")

def about(reqest):
    return render(reqest, "about.html")

def contact(reqest):
    return render(reqest, "contact.html")