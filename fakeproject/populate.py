import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakeproject.settings')
django.setup()
from faker import Faker
from myapp.models import student
f = Faker('en-IN')
def populate(n):
    for i in range(n):
        fname = f.name()
        fage = f.random_int(min =18 , max = 60 )
        femail = f.email()
        fplace= f.address()
        e= student.objects.get_or_create(name = fname,age = fage , email = femail , place = fplace)
populate(20)


