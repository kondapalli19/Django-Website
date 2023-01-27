from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    #messages.success(request, "this is for testing")
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is aboutpage")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        email = request.POST.get('mail')
        password = request.POST.get('password')
        contact = Contact(email=email, password=password, date=datetime.today())
        contact.save()
        messages.success(request, 'Form has been submitted')
    return render(request, 'contact.html')
    #return HttpResponse("This is contact us page")

