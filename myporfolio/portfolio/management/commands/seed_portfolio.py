from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from portfolio.models import Certificate, ContactMessage, Project, ProjectCategory, Resume, Skill


class Command(BaseCommand):
    help = 'Seed the portfolio app with sample data.'

    def handle(self, *args, **options):
        self.stdout.write('Creating initial portfolio data...')

        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass123')
            self.stdout.write('Created admin user: admin')

        Skill.objects.all().delete()
        skills = [
            {'name': 'Python', 'proficiency': 95, 'category': 'Languages'},
            {'name': 'Django', 'proficiency': 92, 'category': 'Backend'},
            {'name': 'HTML', 'proficiency': 90, 'category': 'Frontend'},
            {'name': 'CSS', 'proficiency': 87, 'category': 'Frontend'},
            {'name': 'JavaScript', 'proficiency': 82, 'category': 'Frontend'},
            {'name': 'Bootstrap', 'proficiency': 88, 'category': 'Tools'},
            {'name': 'SQL', 'proficiency': 80, 'category': 'Backend'},
            {'name': 'Git', 'proficiency': 85, 'category': 'Tools'},
        ]
        for item in skills:
            Skill.objects.create(**item)

        ProjectCategory.objects.all().delete()
        projects_data = [
            {'title': 'Django Portfolio', 'description': 'A complete portfolio website with authentication, contact forms, and dynamic project management.', 'technologies': 'Django, Bootstrap, JavaScript', 'github_url': 'https://github.com/example/portfolio', 'demo_url': 'https://example.com', 'published': True},
            {'title': 'Task Tracker', 'description': 'A web app for managing to-do items with categories and progress tracking.', 'technologies': 'Django, SQLite, CSS', 'github_url': 'https://github.com/example/task-tracker', 'demo_url': 'https://example.com/task-tracker', 'published': True},
        ]
        category = ProjectCategory.objects.create(title='Web App')
        for item in projects_data:
            Project.objects.create(category=category, **item)

        Certificate.objects.all().delete()
        Certificate.objects.create(title='Django Web Development', organization='Online Academy', issue_date='2024-01-15', certificate_url='https://example.com/certificate')
        Certificate.objects.create(title='Full Stack Development', organization='Skill Institute', issue_date='2023-08-20', certificate_url='https://example.com/certificate2')

        Resume.objects.all().delete()
        resume = Resume.objects.create(
            education='B.Sc. Computer Science\nUniversity of Example\n2020 - 2024',
            experience='Full Stack Developer intern at Company X\nWeb Developer at Company Y',
            skills='Python, Django, HTML, CSS, JavaScript, Bootstrap, SQLite',
            achievements='Completed multiple client portfolio projects. Delivered responsive web applications on time.',
        )
        resume.certificates.set(Certificate.objects.all())

        ContactMessage.objects.create(name='Jane Doe', email='jane@example.com', subject='Project inquiry', message='I would like to work on a new web app with you.')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully.'))
