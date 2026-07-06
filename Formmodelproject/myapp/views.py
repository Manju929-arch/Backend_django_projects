from django.shortcuts import render
from myapp.forms import StudentForm

# Create your views here.
def formview(request):
    f = StudentForm()

    if request.method == "POST":
        f = StudentForm(request.POST)

        if f.is_valid():
            f.save()

            name = f.cleaned_data['name']
            age = f.cleaned_data['age']
            email = f.cleaned_data['email']
            place = f.cleaned_data['place']

            d = {
                'name': name,
                'age': age,
                'email': email,
                'place': place
            }

            return render(request, 'output.html', d)

    d = {'form': f}
    return render(request, 'form.html', d)