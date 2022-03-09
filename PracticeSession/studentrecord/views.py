from django.shortcuts import render
from .models import studrecords
# Create your views here.

def studdetails(request):

    records = studrecords.objects.all()
    return  render(request,'stdetails.html',{'rec':records})