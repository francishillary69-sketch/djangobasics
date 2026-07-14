from decimal import Decimal

from django.shortcuts import render

from storeapp.models import Employee


def home(request):
    saved = False

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone_number = request.POST.get('phone_number', request.POST.get('phone', '')).strip()
        gender = request.POST.get('gender', '').strip()
        department = request.POST.get('department', '').strip()
        job_title = request.POST.get('job_title', request.POST.get('title', '')).strip()
        salary = request.POST.get('salary', '').strip()
        hire_date = request.POST.get('hire_date', '').strip()
        address = request.POST.get('address', '').strip()

        if all([name, email, phone_number, gender, department, job_title, salary, hire_date, address]):
            Employee.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                gender=gender,
                department=department,
                job_title=job_title,
                salary=Decimal(salary),
                hire_date=hire_date,
                address=address,
            )
            saved = True

    return render(request, 'index.html', {'saved': saved})


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


def products(request):
    return render(request, 'products.html')

