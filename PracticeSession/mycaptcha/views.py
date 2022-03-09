from django.shortcuts import render
from .forms import MyForm
# Create your views here.
def home(request):
   if request.method=="POST":
      form=MyForm(request.POST)
      if form.is_valid():
         print("success")
      else:
         print("fail")
   form=MyForm()
   return render(request,"home.html",{"form":form})