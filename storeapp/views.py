from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')
