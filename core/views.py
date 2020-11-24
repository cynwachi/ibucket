from django.shortcuts import render

# Create your views here.
def viewHompage(request):
    return render(request, "pages/homepage.html")

def addBucket(request):
    return render(request, "pages/pray_play.html")