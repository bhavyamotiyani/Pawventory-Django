from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import User

def register_page(request: HttpRequest):
    msg = ""

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        dob = request.POST.get('dob')
        pwd = request.POST.get('pwd')
        c_pwd = request.POST.get('c_pwd')
        gender = request.POST.get('gender')

        if not all([name, email, contact_no, dob, pwd, c_pwd, gender]):
            msg = "All fields are required"

        elif len(contact_no) != 10:
            msg = "Contact number must be 10 digits"

        elif pwd != c_pwd:
            msg = "Passwords do not match"

        elif User.objects.filter(email=email).exists():
            msg = "Email already registered"

        elif User.objects.filter(contact_no=contact_no).exists():
            msg = "Contact number already registered"

        else:
            User.objects.create(
                name=name,
                email=email,
                contact_no=contact_no,
                dob=dob,
                pwd=pwd,
                gender=gender
            )
            return redirect('login_page')

    return render(request, 'register.html', {'msg': msg})


def login_page(request: HttpRequest):
    msg = ""

    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        user = User.objects.filter(email=email, pwd=pwd).first()

        if user:
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return redirect('home_page')
        else:
            msg = "Invalid email or password"

    return render(request, 'login.html', {'msg': msg})

def home_page(request: HttpRequest):
    if not request.session.get('user_id'):
        return redirect('login_page')

    return render(request, 'home.html', {
        'user_name': request.session.get('user_name')
    })


def logout_page(request: HttpRequest):
    request.session.flush()
    return redirect('login_page')
