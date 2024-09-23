#from django.http import HttpResponse

from django.shortcuts import render



quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Do not wait to strike till the iron is hot, but make it hot by striking.",
    "Success is not how high you have climbed, but how you make a positive difference to the world."
]

images = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg"
]

def base(request):
   
    return render(request, 'base.html')

def homepage(request):
    
    return render(request, 'quote.html')

def about(request):
    
    return render(request, 'about.html')

def show_all(request):
    
    return render(request, 'show_all.html')
