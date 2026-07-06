from django.shortcuts import render
from .models import Contact
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'Base.html')

@login_required
def home(request):
    return render(request, "home.html")

@login_required
def about_view(request):
    return render(request, "about.html")


@login_required
def project(request):
    return render(request, "projects.html")


@login_required
def certificate_view(request):
    return render(request, "certification.html")


@login_required
def contact(request):
    return render(request, "contact.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, "contact.html", {"success": True})

    return render(request, "contact.html")