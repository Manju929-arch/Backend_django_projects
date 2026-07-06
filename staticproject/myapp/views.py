from django.shortcuts import render

# Create your views here.
def myview(request):
    name = "RAMA"
    animal = "Rabbit"
    bird = "Parrot"
    ctx = { 'name':name, 'animal':animal, 'bird':bird}
    return render(request,'fav.html',ctx)

