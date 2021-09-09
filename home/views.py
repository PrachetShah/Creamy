from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("This is Home Page from Home App")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")

