from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_view(request):
    context = {}
    return render(request, "blog/auth/register.html", context)

def login_view(request):
    context = {}
    return render(request, "blog/auth/login.html", context)