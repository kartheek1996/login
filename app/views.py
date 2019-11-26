from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Register
from .forms import Registerform


def register(request):
    form = Registerform()
    return render(request, "register.html", {"form": form})


def savedata(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        password = request.POST["password"]
        Cpassword = request.POST["Cpassword"]
        email = request.POST["email"]

        if Register.objects.filter(username=fname + lname).exists():
            messages.info(request, "username is taken")
            redirect("register")

        else:
            if Register.objects.filter(email=email).exists():
                messages.info(request, "email is taken")
                redirect("register")

            else:
                if password == Cpassword:
                    Register(username=(fname + lname).lower(), password=password, email=email.lower()).save()
                    return render(request, "main.html")
                else:
                    messages.info(request, "password not matching")
                    redirect("register")

    else:
        redirect("register")
    return redirect("register")
