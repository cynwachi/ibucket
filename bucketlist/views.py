from django.shortcuts import render, redirect, get_object_or_404
from .models import User, PrayPlay
from .forms import PrayPlayForm 
#receives messages from urls.py and models.py and from the Template loacated at filename.html
# Create your views here.


def home_page(request): 
    plays = [play.text for play in PrayPlay.objects.filter(type="play")]
    prays = [pray.text for pray in PrayPlay.objects.filter(type="pray")]
    return render (request, "pages/homepage.html", 
                   {"plays": plays, "prays": prays})
    #make template to match this

def list_users(request):
    users = User.objects.all()
    return render (request, "users/list_users.html",
                   {"users": users})
    
# def add_user(request):
#     if request.method == 'GET':
#         form = UserForm()
#     else:
#         form = UserForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='list_contacts')
        
#     return render(request, "users/add_user.html", {"form": form})

def add_pray(request, pk):
    if request.method == "POST":
      form = PrayPlayForm(data=request.POST)
      if form.is_valid():
        prayplay = forms.save(commit=False)
        prayplay.user=request.user
    return redirect(to="user_detail", pk=pk)

# def edit_user(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == 'GET':
#         form = UserForm(instance=user)
#     else:
#         form = UserForm(instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect(to='list_users')
    
    return render(request, "users/edit_user.html", {
        "form": form,
        "user": user
        
    })
    
# 
# 