from django.db import models


class SkillCategory(models.TextChoices):
    FRONTEND = 'Frontend', 'Frontend'
    BACKEND = 'Backend', 'Backend'
    TOOLS = 'Tools', 'Tools'
    LANGUAGES = 'Languages', 'Languages'


class Skill(models.Model):
    name = models.CharField(max_length=120)
    proficiency = models.PositiveIntegerField(default=70)
    category = models.CharField(max_length=20, choices=SkillCategory.choices, default=SkillCategory.TOOLS)
    icon = models.CharField(max_length=120, blank=True, help_text='CSS class or icon name')

    class Meta:
        ordering = ['category', '-proficiency', 'name']

    def __str__(self):
        return self.name


class ProjectCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technologies = models.CharField(max_length=250)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=180)
    organization = models.CharField(max_length=180)
    issue_date = models.DateField()
    certificate_url = models.URLField(blank=True)

    class Meta:
        ordering = ['-issue_date']

    def __str__(self):
        return f"{self.title} - {self.organization}"


class Resume(models.Model):
    education = models.TextField(help_text='JSON or plain text timeline items')
    experience = models.TextField(help_text='JSON or plain text timeline items')
    skills = models.TextField(help_text='Comma-separated skill labels')
    achievements = models.TextField(blank=True)
    certificates = models.ManyToManyField(Certificate, blank=True)
    resume_file = models.FileField(upload_to='resume_files/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Resume data'


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Message from {self.name} <{self.email}>"
