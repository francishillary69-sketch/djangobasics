from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def contact(request):
    success = False

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            success = True

    return render(request, 'contacts.html', {'success': success})


def about(request):
    return render(request, 'about.html')


def gallery(request):
    return render(request, 'gallery.html')


def services(request):
    return render(request, 'services.html')

def contact(request):

    return render(request, 'contact.html')

def products(request):
    return render(request, 'products.html')

