from django.shortcuts import render

def formview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print(name)

    return render(request, 'form.html')