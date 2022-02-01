from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from contacts.models import Contact


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid login credentials")
            return redirect("login")
    return render(request, "accounts/login.html")


def signup(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect("signup")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email already exists")
                    return redirect("signup")
                else:
                    user = User.objects.create_user(
                        first_name=firstname,
                        last_name=lastname,
                        username=username,
                        email=email,
                        password=password
                    )
                    auth.login(request, user)
                    messages.success(request, "You are now logged in")
                    return redirect("dashboard")
                    user.save()
                    messages.success(request, "You are registered successfully.")
                    redirect("login")
        else:
            messages.error(request, "password do not match")
            return redirect("signup")
    else:
        return render(request, "accounts/signup.html")


@login_required(login_url="login")
def dashboard(request):
    user = request.user
    inquired_cars = Contact.objects.order_by("-created_at").filter(user_id=request.user.id)
    context = {
        "inquired_cars": inquired_cars,
    }
    return render(request, "accounts/dashboard.html", context)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("home")
    return redirect("home")
