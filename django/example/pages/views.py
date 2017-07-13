from django.shortcuts import render

# Create your views here.


def home(request):
    names = ["John", "Jacob", "Jingleheimer", "Schmidt"]
    return render(request, "pages/home.html", {'names': names})
