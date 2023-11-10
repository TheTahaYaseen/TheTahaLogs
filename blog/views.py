from django.shortcuts import render

# Create your views here.
def register_view(request):
    context = {}
    return render(request, "templates/blog/auth/register.html", context)

def login_view(request):
    context = {}
    return render(request, "templates/blog/auth/login.html", context)