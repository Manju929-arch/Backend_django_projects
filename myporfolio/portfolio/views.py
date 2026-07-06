from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from accounts.forms import ProfileUpdateForm, UserUpdateForm
from accounts.models import Profile
from portfolio.forms import ContactForm
from portfolio.models import Certificate, Project, Resume, Skill, ContactMessage


def home(request):
    skills = Skill.objects.all()[:8]
    projects = Project.objects.filter(published=True)[:6]
    certificates = Certificate.objects.all()[:4]
    contact_form = ContactForm()
    return render(request, 'portfolio/home.html', {
        'skills': skills,
        'projects': projects,
        'certificates': certificates,
        'contact_form': contact_form,
    })


def about(request):
    skills = Skill.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'portfolio/about.html', {
        'skills': skills,
        'certificates': certificates,
    })


def projects(request):
    projects = Project.objects.filter(published=True)
    query = request.GET.get('query')
    category = request.GET.get('category')
    if query:
        projects = projects.filter(title__icontains=query)
    if category:
        projects = projects.filter(category__title__iexact=category)
    categories = {project.category for project in projects if project.category}
    return render(request, 'portfolio/projects.html', {
        'projects': projects,
        'categories': categories,
        'query': query,
        'category': category,
    })


def resume(request):
    resume_item = Resume.objects.first()
    return render(request, 'portfolio/resume.html', {
        'resume': resume_item,
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'portfolio/contact.html', {
                'form': ContactForm(),
                'success': True,
            })
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})


@login_required
def dashboard(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    recent_messages = ContactMessage.objects.order_by('-submitted_at')[:3]
    return render(request, 'portfolio/dashboard.html', {
        'profile': profile,
        'recent_messages': recent_messages,
    })


@login_required
def update_profile(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('dashboard'))
    return render(request, 'portfolio/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
