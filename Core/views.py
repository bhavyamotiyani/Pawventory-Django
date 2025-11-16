from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
import re
from .models import *

def register_page(request : HttpRequest):

    msg = ""
    popup = False 

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        dob = request.POST.get('dob')
        pwd = request.POST.get('pwd')
        c_pwd = request.POST.get('c_pwd')
        gender = request.POST.get('gender')

        if not all([name,email,contact_no,dob,pwd,c_pwd,gender]): 
            msg = "All fields are required!"
            popup = True

        else:
            email_verify = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            password_verify = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{8,}$'

            if len(contact_no) != 10:
                msg = "Contact no must be of 10 digits"
                popup = True

            elif not re.match(email_verify, email):
                msg = "Email not Valid"
                popup = True
            
            elif not re.match(password_verify,pwd):
                msg = "Password must contain, atleast uppercase, lowercase, digit, special character"
                popup = True

            elif pwd != c_pwd:
                msg = "Password does not match"
                popup = True
        
            else:
                user.objects.create(
                    name=name,
                    email=email,
                    contact_no=contact_no,
                    dob=dob,
                    pwd=pwd,
                    gender=gender
                )
                msg = "Register Done"
                popup = True

                return redirect('login_page')

    return render(request, 'register.html',{"msg":msg , "popup":popup})


def login_page(request : HttpRequest):

    msg = ""
    popup = False 

    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')

        myuser = user.objects.filter(email=email, pwd=pwd).first()

        if myuser:
            msg = f"Welcome {myuser.name}, you have logged in successfully."
            popup = True

            request.session['user_id'] = myuser.id
            request.session['user_name'] = myuser.name

            return redirect("home_page")        

        else:
            msg = "Invalid email or password."
            popup = True

    return render(request, 'login.html', {"msg": msg, "popup": popup})

def home_page(request : HttpRequest):
    return render(request, 'home.html')

