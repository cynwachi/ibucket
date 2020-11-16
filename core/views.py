from django.shortcuts import render

# Create your views here.
def viewHompage(request):
    return render(request, "pages/homepage.html")