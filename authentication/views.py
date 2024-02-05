from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout, authenticate

# Create your views here.
def register_view(request):
    error = ""
    form_action = "Register"

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not username or not password:
            error = "Please fill out both fields!"
        elif len(password) < 8:
            error = "Password must be longer than 8 characters!"
        else:
            try:
                user = User.objects.get(username=username)
                error = "User with username already exists!"
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)    
                return redirect("home")

    context = {"form_action": form_action, "error": error}
    return render(request, "auth_form.html", context)

def login_view(request):
    error = ""
    form_action = "Login"

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not username or not password:
            error = "Please fill out both fields!"
        else:
            try:
                user = User.objects.get(username=username)

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)    
                    return redirect("home")
                else:
                    error = "Invalid credentials!"

            except User.DoesNotExist:
                error = "User with username does not exist!"

    context = {"form_action": form_action, "error": error}
    return render(request, "auth_form.html", context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")