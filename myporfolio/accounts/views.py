from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse

from accounts.forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your account has been created. You may now log in.')
            return redirect(reverse('login'))
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
