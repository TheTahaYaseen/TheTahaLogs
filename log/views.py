from django.shortcuts import redirect, render

from .models import Log

# Create your views here.

def logs_view(request):
    if request.user.is_superuser:
        logs = Log.objects.all().order_by("-created")
    else:
        logs = Log.objects.filter(visibility="Public")

    context = {"logs": logs}
    return render(request, "logs.html", context)

def add_view(request):
    form_action = "Add"
    error = ""

    if not request.user.is_superuser:
        return redirect("home")

    subject, log = "", ""

    if request.method == "POST":
        subject = request.POST.get("subject")
        log = request.POST.get("log")
        visibility = request.POST.get("visibility")

        if not subject or not log:
            error = "Please fill out both fields!"
        elif len(subject) > 255:
            error = "Subject cannot be longer than 255 characters!"
        else:
            log = Log.objects.create(subject=subject, log=log, visibility=visibility)
            return redirect("logs")

    context = {"form_action": form_action, "error": error, "subject": subject, "log": log}
    return render(request, "log_form.html", context)

def update_view(request, log_id):
    form_action = "Update"
    error = ""

    if not request.user.is_superuser:
        return redirect("home")

    associated_log = Log.objects.get(id=log_id)
    subject, log, visibility = associated_log.subject, associated_log.log, associated_log.visibility

    if request.method == "POST":
        subject = request.POST.get("subject")
        log = request.POST.get("log")
        visibility = request.POST.get("visibility")

        if not subject or not log:
            error = "Please fill out both fields!"
        elif len(subject) > 255:
            error = "Subject cannot be longer than 255 characters!"
        else:
            associated_log.subject = subject
            associated_log.log = log
            associated_log.visibility = visibility
            associated_log.save()
            return redirect("logs")

    context = {"form_action": form_action, "error": error, "subject": subject, "log": log}
    return render(request, "log_form.html", context)

def delete_view(request, log_id):
    associated_log = Log.objects.get(id=log_id)
    associated_log.delete()
    return redirect("logs")