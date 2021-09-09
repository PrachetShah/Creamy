from django.shortcuts import render, HttpResponse
from home.models import Contact
import datetime
# TO send messages
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is Home Page from Home App")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        
        contact = Contact(name=name, email=email, text=text, date=datetime.datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!!')
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")

