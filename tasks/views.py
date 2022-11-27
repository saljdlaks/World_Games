from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Profile

# Create your views here.


def login(request):
    return render(request, "login.html")


def sign_up(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Nombre de usuario ya está en uso")
            return redirect("/login?st=sign-up")
        elif User.objects.filter(email=email).exists():
            messages.warning(request, "Correo ya está en uso")
            return redirect("/login?st=sign-up")
        else:
            try:
                user = User.objects.create_user(
                    username=username, password=password, email=email
                )
                user_p = Profile.objects.create(name=name)
                user.save()
                user_p.save()
                messages.success(request, "¡Usuario creado con éxito!")
                return redirect("/")
            except:
                messages.warning(request, "Ingresa datos válidos por favor")
                return redirect("/login?st=sign-up")
    else:
        return render(request, "login.html")


def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, f"¡Bienvenido {user}!")
            return redirect("/")
        else:
            messages.warning(request, "Nombre de usuario o contraseña inválido")
            return redirect("/login")
    else:
        return render(request, "login.html")


def logout_user(request):
    auth.logout(request)
    messages.info(request, "Has cerrado sesión")
    return redirect("/")
